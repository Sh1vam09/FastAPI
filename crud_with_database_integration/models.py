from database import Base
from sqlalchemy import Column, Integer, String


class Employee(Base):
    __tablename__ = "employee"  # name of the table is define like this
    id = Column(
        Integer, primary_key=True, index=True
    )  # index=true means to retrive info fatser
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
