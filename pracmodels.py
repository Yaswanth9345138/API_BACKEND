from sqlalchemy import Column,Integer,String
from pracdatabase import Base 

class pracstudb(Base):
    __tablename__="pracstu"

    stuid=Column(Integer,primary_key=True)
    stuname=Column(String)
    stuage=Column(Integer)
    course=Column(String)
    email=Column(String)
    passw=Column(String)