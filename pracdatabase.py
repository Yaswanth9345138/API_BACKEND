from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv
load_dotenv()
a=os.getenv("a")
b=os.getenv("b")
c=os.getenv("c")
d=os.getenv("d")
p=int(os.getenv("port"))


url=URL.create(
    "mysql+pymysql",
    username=b,
    password=c,
    host=a,
    database=d,
    port=p
)


e1 = create_engine(
    url,
    connect_args={"ssl": {"ca": "ca.pem"}}
)

s1=sessionmaker(bind=e1)
Base=declarative_base()

def get_db():
    db=s1()
    try:
        yield db
    finally:
        db.close()
