from fastapi import FastAPI,Depends,HTTPException
from database import get_db
from models import StudentDB
from schemas import Student 

app = FastAPI()
 
@app.post("/students")
def create_student(student: Student, db=Depends(get_db)):
    new_student = StudentDB(
        name=student.name,
        age=student.age
    )
    db.add(new_student)
    db.commit()
    return new_student

@app.get("/students",response_model=list[Studentresponse])
def get_students(db=Depends(get_db)):
    students = db.query(StudentDB).all()
    if students is None:
        raise HTTPException(status_code=404,detail="data not found")
    return students


@app.get("/students/{student_id}",response_model=Studentresponse)
def get_student(student_id: int, db=Depends(get_db)):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

@app.put("/students/{student_id}",response_model=Studentresponse)
def update_student(student_id: int, student: Student,db=Depends(get_db)):
    existing = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if existing is None:
        raise HTTPException(status_code=404, detail="Student not found")

    existing.name = student.name
    existing.age = student.age

    db.commit()
    return existing

@app.delete("/students/{student_id}")
def delete_student(student_id: int,db=Depends(get_db)):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}