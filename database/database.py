# database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://ecs_api_user:password@localhost/ecs_api"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#! UNCOMMENT THIS TO TEST IF YOU CAN CONNECT TO DB
"""
if __name__ == "__main__":
    try:
        get_db()
        print("Successfully connected to db")
    except Exception as e:
        print(f"Unable to get db : {e}")
"""