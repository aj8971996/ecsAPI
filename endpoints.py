#! PLACEHOLDER - IN PROGRESS
# api/endpoints.py (Example using FastAPI)
from fastapi import FastAPI
from .database import Session, Employee

app = FastAPI()

@app.get("/employees")
def get_employees():
    session = Session()
    employees = session.query(Employee).all()
    return employees