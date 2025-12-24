from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = (
    "sqlite:///./test.db"  # /. ->in current directory make the databse file
)
# create_engine-> to connect to the database
# connect_args-> allow connection sharing across threads
engine = create_engine(
    SQLALCHEMY_DATABSE_URL, connect_args={"check_same_thread": False}
)

# help to create new database session
# each session reperesent a transaction
# #autoflush will not automatically update it unless you do refresh the objects manually
# #autocommit to not commit whatever chnages we make
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# used to link python classes to database tables
Base = declarative_base()
