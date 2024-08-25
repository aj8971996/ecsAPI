# database/models.py (Using SQLAlchemy as ORM)
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship

# Define the Base here
Base = declarative_base()

# Employee Table (Source Table for item_transactions / Front End Table)
class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)  # Unique identifier for each employee
    emp_first_name = Column(String(50), nullable=False)  # First name of the employee
    emp_last_name = Column(String(50), nullable=False)  # Last name of the employee
    emp_job_title = Column(String(100))  # Job title of the employee
    emp_start_date = Column(Date)  # Start date of the employee's tenure
    emp_checkout_indicator = Column(Boolean, default=False)  # Indicates if the employee has an active checkout
    emp_user_anem = Column(String(50), nullable=False)  # Username for employee login
    emp_password = Column(String(50), nullable=False)  # Password for employee login

    # Relationships
    checkouts = relationship('CheckOut', back_populates='employee')  # Links employee to their checkouts
    checkins = relationship('CheckIn', back_populates='employee')  # Links employee to their check-ins


# Tool Table (Source Table for item_inventory table)
class Tool(Base):
    __tablename__ = 'tools'
    tool_id = Column(Integer, primary_key=True)  # Unique identifier for each tool
    tool_name = Column(String(100), nullable=False)  # Name or description of the tool
    tool_type = Column(String(50))  # Type or category of the tool
    tool_added_to_inventory_date = Column(Date)  # Date when the tool was added to inventory
    tool_cost = Column(Float)  # Cost of the tool
    tool_lost_indicator = Column(Boolean, default=False)  # Indicates if the tool is lost
    tool_out_of_stock_indicator = Column(Boolean, default=False)  # Indicates if the tool is out of stock

    # Relationships
    checkouts = relationship('CheckOut', back_populates='tool')  # Links tool to its checkouts
    checkins = relationship('CheckIn', back_populates='tool')  # Links tool to its check-ins

# Material Table (Source Table for item_inventory table)
class Material(Base):
    __tablename__ = 'materials'
    material_id = Column(Integer, primary_key=True)  # Unique identifier for each material
    material_name = Column(String(100), nullable=False)  # Name or description of the material
    material_type = Column(String(50))  # Type or category of the material
    material_added_to_inventory_date = Column(Date)  # Date when the material was added to inventory
    material_cost = Column(Float)  # Cost of the material
    material_metric = Column(String(50))  # Unit of measurement for the material (e.g., kg, liter)
    material_quantity_available = Column(Integer, default=0)  # Quantity of material currently available in inventory
    material_out_of_stock_indicator = Column(Boolean, default=False)  # Indicates if the material is out of stock

# CheckIn Table (Source Table for item_transactions)
class CheckIn(Base):
    __tablename__ = 'check_ins'
    check_in_id = Column(Integer, primary_key=True)  # Unique identifier for each check-in record
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))  # Reference to the employee who returned the tool
    tool_id = Column(Integer, ForeignKey('tools.tool_id'))  # Reference to the tool being returned
    check_in_date = Column(DateTime, default=datetime.datetime.utcnow)  # Date and time when the tool was returned

    # Relationships
    employee = relationship('Employee', back_populates='checkins')  # Links check-in to the employee
    tool = relationship('Tool', back_populates='checkins')  # Links check-in to the tool


# CheckOut Table (Source Table for item_transactions)
class CheckOut(Base):
    __tablename__ = 'check_outs'
    check_out_id = Column(Integer, primary_key=True)  # Unique identifier for each check-out record
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))  # Reference to the employee who checked out the item
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), nullable=True)  # Reference to the tool being checked out (nullable if material)
    material_id = Column(Integer, ForeignKey('materials.material_id'), nullable=True)  # Reference to the material being issued (nullable if tool)
    check_out_date = Column(DateTime, default=datetime.datetime.utcnow)  # Date and time when the item was checked out
    quantity_issued = Column(Integer, nullable=True)  # Quantity of material issued (only applicable for materials)

    # Relationships
    employee = relationship('Employee', back_populates='checkouts')  # Links check-out to the employee
    tool = relationship('Tool', back_populates='checkouts')  # Links check-out to the tool
    material = relationship('Material')  # Links check-out to the material


# ItemInventory Table (Source Table for item_transactions / Front End Table)
class ItemInventory(Base):
    __tablename__ = 'item_inventory'
    item_id = Column(Integer, primary_key=True)  # Unique identifier for each inventory item (tool or material)
    item_type = Column(String(50), nullable=False)  # Specifies whether the item is a tool or material
    item_stock = Column(Integer)  # Current stock of the item
    item_out_of_stock_indicator = Column(Boolean)  # Indicates if the item is out of stock
    item_lost_indicator = Column(Boolean)  # Indicates if the item is lost


# Transactions Table (Front End Table)
class Transactions(Base):
    __tablename__ = 'item_transactions'
    transaction_id = Column(Integer, primary_key=True)  # Unique identifier for each transaction record
    transaction_owner_id = Column(Integer)  # Reference to the employee involved in the transaction
    transaction_owner_name = Column(String(100))  # Name of the employee involved in the transaction
    transaction_item_id = Column(Integer)  # Reference to the item being transacted (from item inventory)
    transaction_type = Column(String(50))  # Type of transaction (e.g., Tool Check Out, Material Issued)
    transaction_status = Column(String(50))  # Status of the transaction (e.g., Open, Closed)
    transaction_quantity = Column(Integer, nullable=True)  # Quantity of material issued (applicable for material transactions)
    transaction_open_date = Column(Date)  # Date when the transaction was initiated
    transaction_close_date = Column(Date, nullable=True)  # Date when the transaction was closed (nullable if ongoing)