import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@localhost/'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
while True:
    try:
        conn = psycopg2.connect(host='localhost',database='',user='postgres',password='2002',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Databse Connection was a success")
        break
    except Exception as error:
        print("Databse Connection was failed")
        print("Error is :" ,error)
        time.sleep(2)