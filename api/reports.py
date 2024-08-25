import datetime
from database.models import Employee, Tool, Material, CheckOut, CheckIn, Transactions
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import and_, or_

# 1. Validate Employee Login
def validate_employee_login(db: Session, username: str, password: str):
    employee = db.query(Employee).filter(and_(Employee.emp_user_anem == username, Employee.emp_password == password)).first()
    if not employee:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return employee

# 2. Check Out Tool or Material
def check_out_item(db: Session, employee_id: int, tool_id: int = None, material_id: int = None, quantity: int = 0):
    if tool_id:
        tool = db.query(Tool).filter(Tool.tool_id == tool_id).first()
        if not tool or tool.tool_out_of_stock_indicator:
            raise HTTPException(status_code=400, detail="Tool is out of stock or does not exist")

        # Create a new checkout entry for the tool
        new_checkout = CheckOut(
            employee_id=employee_id,
            tool_id=tool_id,
            check_out_date=datetime.datetime.utcnow()
        )
        db.add(new_checkout)

        # Update the tool inventory status
        tool.tool_out_of_stock_indicator = True

        # Add transaction record
        transaction = Transactions(
            transaction_owner_id=employee_id,
            transaction_owner_name=db.query(Employee.emp_first_name, Employee.emp_last_name).filter(Employee.emp_id == employee_id).first(),
            transaction_item_id=tool_id,
            transaction_type="Tool Check Out",
            transaction_status="Open",
            transaction_open_date=datetime.date.today()
        )
        db.add(transaction)

    elif material_id:
        material = db.query(Material).filter(Material.material_id == material_id).first()
        if not material or material.material_quantity_available < quantity:
            raise HTTPException(status_code=400, detail="Insufficient material quantity or material does not exist")

        # Reduce the material quantity
        material.material_quantity_available -= quantity
        if material.material_quantity_available == 0:
            material.material_out_of_stock_indicator = True

        # Add transaction record
        transaction = Transactions(
            transaction_owner_id=employee_id,
            transaction_owner_name=db.query(Employee.emp_first_name, Employee.emp_last_name).filter(Employee.emp_id == employee_id).first(),
            transaction_item_id=material_id,
            transaction_type="Material Issued",
            transaction_status="Closed",
            transaction_quantity=quantity,
            transaction_open_date=datetime.date.today(),
            transaction_close_date=datetime.date.today()
        )
        db.add(transaction)

    else:
        raise HTTPException(status_code=400, detail="Must provide either a tool_id or material_id")

    db.commit()
    return {"message": "Check out successful"}

# 3. Check In Tool or Material
def check_in_item(db: Session, employee_id: int, tool_id: int = None, material_id: int = None, quantity: int = 0):
    if tool_id:
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

        # Update transaction record
        transaction = db.query(Transactions).filter(
            Transactions.transaction_item_id == tool_id,
            Transactions.transaction_status == "Open"
        ).first()
        if transaction:
            transaction.transaction_status = "Closed"
            transaction.transaction_close_date = datetime.date.today()

    elif material_id:
        material = db.query(Material).filter(Material.material_id == material_id).first()
        if material:
            # If there was an error and material is being returned, increment stock
            material.material_quantity_available += quantity
            if material.material_quantity_available > 0:
                material.material_out_of_stock_indicator = False

        else:
            raise HTTPException(status_code=400, detail="Material does not exist")

    else:
        raise HTTPException(status_code=400, detail="Must provide either a tool_id or material_id")

    db.commit()
    return {"message": "Check in successful"}

# 4. Get Out of Stock Materials
def get_out_of_stock_materials(db: Session):
    out_of_stock_materials = db.query(Material).filter(Material.material_out_of_stock_indicator == True).all()
    return out_of_stock_materials

# 5. Get Lost Tools
def get_lost_tools(db: Session):
    lost_tools = db.query(Tool).filter(Tool.tool_lost_indicator == True).all()
    return lost_tools

# 6. Get Active Checkouts
def get_active_checkouts(db: Session):
    active_checkouts = db.query(CheckOut).filter(CheckOut.check_out_date != None).all()
    return active_checkouts

# 7. Get All Out of Stock Materials (Duplicate to #4, consider removing or refactoring)
def get_all_out_of_stock_materials(db: Session):
    return get_out_of_stock_materials(db)