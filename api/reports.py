# api/reports.py
from database.database import get_db  # Use absolute import
from database.models import Employee, Tool, Material, CheckOut

def generate_employee_list(db):
    employees = db.query(Employee).all()
    return employees

def generate_inventory_list(db):
    tools = db.query(Tool.tool_name, Tool.tool_count, Tool.tool_out_of_stock_indicator).all()
    materials = db.query(Material.material_name, Material.material_count, Material.material_out_of_stock_indicator).all()
    return {"Tools": tools, "Materials": materials}

def generate_open_transactions_report(db):
    open_transactions = db.query(CheckOut).filter(CheckOut.check_out_date != None, CheckOut.material_id == None).all()
    return open_transactions

def generate_active_checkouts_report(db):
    active_checkouts = db.query(Employee).filter(Employee.emp_checkout_indicator == True).all()
    return active_checkouts