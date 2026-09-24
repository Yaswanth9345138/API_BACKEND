from sqlalchemy import Column, Integer, String
from database import Base

class StudentDB(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)