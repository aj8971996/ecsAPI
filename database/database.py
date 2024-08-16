# database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Employee, Tool, Material, CheckIn, CheckOut, ItemInventory, Transactions

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

# Function to create tables
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")

#! UNCOMMENT THIS TO TEST IF YOU CAN CONNECT TO DB
"""
if __name__ == "__main__":
    try:
        get_db()
        print("Successfully connected to db")
    except Exception as e:
        print(f"Unable to get db : {e}")
"""