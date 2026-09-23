from fastapi import FastAPI,String,Column,Integer,Depends
from sqlalchemy import engine
from sqlalchemy.orm import session
app=FastAPI()
@app.get("/")
def basic():
  return{"WELCOME TO DEFAULT MODE!"}
