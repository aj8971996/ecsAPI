# api/reports.py
import datetime
from database.models import Employee, Tool, Material, CheckOut, CheckIn
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import and_

# 1. Validate Employee Login
def validate_employee_login(db: Session, username: str, password: str):
    employee = db.query(Employee).filter(and_(Employee.emp_user_anem == username, Employee.emp_password == password)).first()
    if not employee:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return employee

# 2. Generate Inventory Lists (Already existing)
def generate_inventory_list(db: Session):
    tools = db.query(Tool.tool_name, Tool.tool_count, Tool.tool_out_of_stock_indicator, Tool.tool_lost_indicator).all()
    materials = db.query(Material.material_name, Material.material_count, Material.material_out_of_stock_indicator, Material.material_lost_indicator).all()
    return {"Tools": tools, "Materials": materials}

# 3. Check Out Tools
def check_out_tool(db: Session, employee_id: int, tool_id: int):
    tool = db.query(Tool).filter(Tool.tool_id == tool_id).first()
    if not tool or tool.tool_out_of_stock_indicator:
        raise HTTPException(status_code=400, detail="Tool is out of stock or does not exist")

    # Create a new checkout entry
    new_checkout = CheckOut(
        employee_id=employee_id,
        tool_id=tool_id,
        check_out_date=datetime.datetime.utcnow()
    )
    db.add(new_checkout)

    # Update the tool inventory status
    tool.tool_out_of_stock_indicator = True
    db.commit()

    return new_checkout

# 4. Check In Tools
def check_in_tool(db: Session, employee_id: int, tool_id: int):
    # Find the active checkout entry for this tool
    checkout = db.query(CheckOut).filter(
        CheckOut.employee_id == employee_id,
        CheckOut.tool_id == tool_id,
        CheckOut.check_out_date != None
    ).first()

    if not checkout:
        raise HTTPException(status_code=400, detail="Tool is not checked out")

    # Close the checkout entry by checking in the tool
    new_checkin = CheckIn(
        employee_id=employee_id,
        tool_id=tool_id,
        check_in_date=datetime.datetime.utcnow()
    )
    db.add(new_checkin)

    # Update the tool inventory status
    tool = db.query(Tool).filter(Tool.tool_id == tool_id).first()
    tool.tool_out_of_stock_indicator = False
    db.commit()

    return new_checkin

# 5. Generate Reports

# a. Active Checkouts (Already existing)
def generate_active_checkouts_report(db: Session):
    active_checkouts = db.query(CheckOut).filter(CheckOut.check_out_date != None).all()
    return active_checkouts

# b. Active Lost Items
def generate_active_lost_items_report(db: Session):
    lost_items = db.query(Tool).filter(Tool.tool_lost_indicator == True).all()
    return lost_items