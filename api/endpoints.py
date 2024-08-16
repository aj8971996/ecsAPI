# api/endpoints.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db  # Use absolute import
from schema import EmployeeSchema, ToolSchema, MaterialSchema, CheckInOutSchema, InventorySchema
from typing import List
from api.reports import generate_employee_list, generate_inventory_list, generate_open_transactions_report, generate_active_checkouts_report

app = FastAPI()

@app.get("/employees", response_model=List[EmployeeSchema])
async def read_employees(db: Session = Depends(get_db)):
    try:
        return generate_employee_list(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/inventory")
async def read_inventory(db: Session = Depends(get_db)):
    try:
        inventory = generate_inventory_list(db)
        return inventory
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/open-transactions")
async def read_open_transactions(db: Session = Depends(get_db)):
    try:
        open_transactions = generate_open_transactions_report(db)
        return open_transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/active-checkouts")
async def read_active_checkouts(db: Session = Depends(get_db)):
    try:
        active_checkouts = generate_active_checkouts_report(db)
        return active_checkouts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))