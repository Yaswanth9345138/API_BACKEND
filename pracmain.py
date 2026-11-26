from fastapi import FastAPI,HTTPException,Depends
from pracdatabase import get_db
from pracmodels import pracstudb
from pracschema import pracstudent,pracpatch,pracstulogin,pracstureq
from pwdlib import PasswordHash
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
import jwt
from datetime import datetime,timedelta,timezone
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

import os
from dotenv import load_getenv
load_getenv()


p1=PasswordHash.recommended()
secret=os.getenv("secret")
security=HTTPBearer()

app=FastAPI(title="STUDENT")
algm="HS256"

@app.post("/register")
def reg(s1:pracstudent,db=Depends(get_db)):
    text="yash"
    p2=p1.hash(s1.passw)
    u1=pracstudb(
        stuid=s1.stuid,
        stuname=s1.stuname,
        stuage=s1.stuage,
        course=s1.course,
        email=s1.email,
        passw=p2
    )
    db.add(u1)
    db.commit()
    db.refresh(u1)
    db.close()


@app.post("/login")
def login(s1:pracstulogin,db=Depends(get_db)):
    s2=db.query(pracstudb).filter(pracstudb.stuid==s1.stuid).first()
    if s2 is None:
        raise HTTPException(status_code=404,detail="not found")

    if not p1.verify(s1.passw,s2.passw):
        return{"try again"}

    payload={"student name":s2.stuname,"stuage":s2.stuage,"exp":datetime.now(timezone.utc)+timedelta(seconds=500)}
    token=jwt.encode(payload,secret,algorithm=algm)
    return{"authentication success ":token}


@app.get("/curruser")
def get_curr_user(c1:HTTPAuthorizationCredentials=Depends(security),db=Depends(get_db)):
    token=c1.credentials

    payload=jwt.decode(token,secret,algorithms=[algm])
    
    if payload is None:
        raise HTTPException(status_code=404,detail="not found")
    if payload["exp"]==0:
        raise ExpiredSignatureError
    return payload
    return{"studentname":payload["student name"],"stuage":payload["stuage"]}


@app.get("/profile")
def profile(c1=Depends(get_curr_user)):
    return c1

@app.get("/age19")
def age_19(u1=Depends(get_curr_user)):
    if u1["stuage"]==19:
        raise HTTPException(status_code=404,detail="not found")

    return {"welcome ":u1["student name"]," your age is ":u1["stuage"]   }

    





@app.post("/future req")
def auth(s1:pracstureq,c1:HTTPAuthorizationCredentials=Depends(security),db=Depends(get_db)):
    token=c1.credentials
    payload=jwt.decode(token,secret,algm)
    if payload is None:
        raise HTTPException(status_code=401,detail="no payload")
    sname=payload["student name"]
    if sname!="shinchan":
        return {"get lost"}
    return {"token generated successfully , you're welcome sir !!!"}


@app.get("/wish/{id}")
def wish(id:int,db=Depends(get_db)):
    s1=db.query(pracstudb).filter(pracstudb.stuid==id).first()
    if s1 is None:
        return{"welcome":"new user"}
    return {"name":s1.stuname,"age":s1.stuage}


l1=[]
@app.get("/students/cse")
def getcsestu(db=Depends(get_db)):
    s2=db.query(pracstudb).filter(pracstudb.course=="CSE")
    for i in s2:
        l1.append(i.stuname)
    return l1

@app.patch("/studata")
def patch(s1:pracpatch,db=Depends(get_db)):
    s3=db.query(pracstudb).filter(pracstudb.stuid==s1.stuid).first()

    s3.stuage=s1.stuage
    s3.course=s1.course
    db.commit()
    db.close
        
@app.put("/modify")
def modify(s2:pracstudent,db=Depends(get_db)):
    s3=db.query(pracstudb).filter(pracstudb.stuid==s2.stuid).first()

    s3.stuname=s2.stuname
    s3.stuage=s2.stuage
    s3.course=s2.course    
    s3.email=s2.email

    db.commit()

@app.delete("/delete")
def delstu(s1:pracstudent,db=Depends(get_db)):
    s2=db.query(pracstudb).filter(pracstudb.stuid==s1.stuid).first()
    if s2 is None:
        raise HTTPException(status_code=404,detail="user not found")

    u1=pracstudb(
        stuid=s2.stuid,
        stuname=s2.stuname,
        stuage=s2.stuage,
        course=s2.course,
        email=s2.email
    )
    db.delete(s2)
    db.commit()
    



@app.post("/postdata")
def postdata(s1:pracstudent,db=Depends(get_db)):
    s1=pracstudb(
        stuid=s1.stuid,
        stuname=s1.stuname,
        stuage=s1.stuage,
        course=s1.course,
        email=s1.email
        )    
    s2=db.query(pracstudb).filter(pracstudb.email==s1.email).first()
    if s2 is None:
        db.add(s1)
    else:
        raise  HTTPException(status_code=400,detail="user already exisisting")
    
    db.commit()
    db.close()


