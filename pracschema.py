from pydantic import BaseModel
from pracmodels import pracstudb


class pracstudent(BaseModel):
    stuid:int
    stuname:str
    stuage:int
    course:str
    email:str
    passw:str

class pracpatch(BaseModel):
    stuid:int
    stuage:int
    course:str

class pracstulogin(BaseModel):
    stuid:int
    passw:str

class pracstureq(BaseModel):
    stuid:int
    stuname:str

