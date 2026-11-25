from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import URL

url=URL.create(
    "mysql+pymysql",
    username="root",
    password="Yaswanth@138",
    host="localhost",
    database="pracstudent_db"
)

e1=create_engine(url)
s1=sessionmaker(bind=e1)
Base=declarative_base()

def get_db():
    db=s1()
    try:
        yield db
    finally:
        db.close()
