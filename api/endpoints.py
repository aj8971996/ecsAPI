from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schema import EmployeeSchema, ToolSchema, MaterialSchema, TransactionSchema, InventorySchema
from typing import List
from api.reports import (
    validate_employee_login, check_out_item, check_in_item,
    get_out_of_stock_materials, get_lost_tools, get_active_checkouts, get_inventory
)

app = FastAPI()

# Endpoint to validate employee login
@app.post("/login", response_model=EmployeeSchema)
async def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        return validate_employee_login(db, username, password)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to check out a tool or material
@app.post("/checkout", response_model=TransactionSchema)
async def checkout_item(employee_id: int, tool_id: int = None, material_id: int = None, quantity: int = 0, db: Session = Depends(get_db)):
    try:
        return check_out_item(db, employee_id, tool_id, material_id, quantity)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to check in a tool or material
@app.post("/checkin", response_model=TransactionSchema)
async def checkin_item(employee_id: int, tool_id: int = None, material_id: int = None, quantity: int = 0, db: Session = Depends(get_db)):
    try:
        return check_in_item(db, employee_id, tool_id, material_id, quantity)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all out of stock materials
@app.get("/materials/out-of-stock", response_model=List[MaterialSchema])
async def get_out_of_stock_materials_endpoint(db: Session = Depends(get_db)):
    try:
        return get_out_of_stock_materials(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all lost tools
@app.get("/tools/lost", response_model=List[ToolSchema])
async def get_lost_tools_endpoint(db: Session = Depends(get_db)):
    try:
        return get_lost_tools(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all active checkouts
@app.get("/checkouts/active", response_model=List[TransactionSchema])
async def get_active_checkouts_endpoint(db: Session = Depends(get_db)):
    try:
        return get_active_checkouts(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get the full inventory
@app.get("/inventory", response_model=List[InventorySchema])
async def get_inventory_endpoint(db: Session = Depends(get_db)):
    try:
        return get_inventory(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
