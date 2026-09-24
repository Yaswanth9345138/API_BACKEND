from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

url = URL.create(
    "mysql+pymysql",
    username="root",
    password="Yaswanth@138",
    host="localhost",
    database="student_db"
)

engine = create_engine(url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  