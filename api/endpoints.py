from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Tool
from schema import EmployeeSchema, ToolSchema, MaterialSchema, TransactionSchema, InventorySchema, RefillRequestSchema
from typing import List
from api.reports import (
    validate_employee_login, check_out_item, check_in_item,
    get_out_of_stock_materials, get_lost_tools, get_active_checkouts, 
    get_inventory, mark_tool_as_lost, refill_tool, get_all_refill_requests
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

# Endpoint to mark a tool as lost
@app.post("/tools/lost/{tool_id}")
async def mark_tool_as_lost_endpoint(tool_id: int, db: Session = Depends(get_db)):
    try:
        return mark_tool_as_lost(db, tool_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to post a Refill Tool request
@app.post("/refill", response_model=dict)
async def refill_tool_endpoint(employee_id: int, item_id: int, request_type: str, db: Session = Depends(get_db)):
    try:
        return refill_tool(db, employee_id, item_id, request_type)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to view all refill requests
@app.get("/refill/requests", response_model=List[RefillRequestSchema])
async def get_refill_requests_endpoint(db: Session = Depends(get_db)):
    try:
        return get_all_refill_requests(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Endpoint to add a new tool
@app.post("/tools/add", response_model=ToolSchema)
async def add_new_tool(tool: ToolSchema, db: Session = Depends(get_db)):
    try:
        new_tool = Tool(
            tool_name=tool.tool_name,
            tool_type=tool.tool_type,
            tool_added_to_inventory_date=tool.tool_added_to_inventory_date,
            tool_cost=tool.tool_cost,
            tool_lost_indicator=False,  # New tools are not lost by default
            tool_out_of_stock_indicator=False  # New tools are in stock by default
        )
        db.add(new_tool)
        db.commit()
        db.refresh(new_tool)
        return new_tool
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to mark a lost tool as replaced
@app.post("/tools/replaced/{tool_id}")
async def mark_tool_as_replaced(tool_id: int, db: Session = Depends(get_db)):
    try:
        tool = db.query(Tool).filter(Tool.tool_id == tool_id).first()
        if not tool:
            raise HTTPException(status_code=404, detail="Tool not found")
        
        tool.tool_lost_indicator = False  # Mark tool as not lost
        db.commit()
        return {"message": "Tool marked as replaced"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))