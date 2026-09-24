from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

class Studentresponse(BaseModel):
    id:int
    name:str
    age:int