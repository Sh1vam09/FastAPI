from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import redis
import json
import hashlib

app = FastAPI()


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True  # so Redis returns strings, not bytes
)

DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    if db.query(User).count() == 0:
        db.add_all([
            User(id=1, name="Michael", age=45),
            User(id=2, name="Jim", age=35),
            User(id=3, name="Pam", age=27),
        ])
        db.commit()
    db.close()


init_db()


class UserQuery(BaseModel):
    user_id: int


def make_cache_key(user_id: int) -> str:
    raw = f"user:{user_id}"
    return "DB:" + hashlib.sha256(raw.encode()).hexdigest()


@app.post("/get-user")
def get_user(query: UserQuery, db: Session = Depends(get_db)):
    cache_key = make_cache_key(query.user_id)

    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("Serving from Redis cache")
        return json.loads(cached_data)

    user = db.query(User).filter(User.id == query.user_id).first()

    if not user:
        return {"message": "User not found"}

    result = {
        "id": user.id,
        "name": user.name,
        "age": user.age
    }
    redis_client.set(cache_key, json.dumps(result), ex=3600)
    print("Fetched from DB and cached")

    return result
