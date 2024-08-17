# database/models.py (Using SQLAlchemy as ORM)
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship

# Define the Base here
Base = declarative_base()

# Employee Table (Source Table for item_transactions / Front End Table)
class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)  # Primary Key
    emp_first_name = Column(String(50), nullable=False)  # Specify length for VARCHAR
    emp_last_name = Column(String(50), nullable=False)  # Specify length for VARCHAR
    emp_job_title = Column(String(100))  # Specify length for VARCHAR
    emp_start_date = Column(Date)
    emp_checkout_indicator = Column(Boolean, default=False)
    
    # Relationships
    checkouts = relationship('CheckOut', back_populates='employee')
    checkins = relationship('CheckIn', back_populates='employee')


# Tool Table (Source Table for item_inventory table)
class Tool(Base):
    __tablename__ = 'tools'
    tool_id = Column(Integer, primary_key=True)  # Primary Key
    tool_name = Column(String(100), nullable=False)  # Specify length for VARCHAR
    tool_type = Column(String(50))  # Specify length for VARCHAR
    tool_added_to_inventory_date = Column(Date)
    tool_cost = Column(Float)
    tool_count = Column(Integer)
    tool_out_of_stock_indicator = Column(Boolean, default=False)
    
    # Relationships
    checkouts = relationship('CheckOut', back_populates='tool')
    checkins = relationship('CheckIn', back_populates='tool')


# Material Table (Source Table for item_inventory table)
class Material(Base):
    __tablename__ = 'materials'
    material_id = Column(Integer, primary_key=True)  # Primary Key
    material_name = Column(String(100), nullable=False)  # Specify length for VARCHAR
    material_type = Column(String(50))  # Specify length for VARCHAR
    material_added_to_inventory_date = Column(Date)
    material_cost = Column(Float)
    material_count = Column(Integer)
    material_metric = Column(String(50))  # Specify length for VARCHAR
    material_out_of_stock_indicator = Column(Boolean, default=False)
    
    # Relationships
    checkouts = relationship('CheckOut', back_populates='material')
    checkins = relationship('CheckIn', back_populates='material')


# CheckIn Table (Source Table for item_transactions)
class CheckIn(Base):
    __tablename__ = 'check_ins'
    check_in_id = Column(Integer, primary_key=True)  # Primary Key
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), nullable=True)
    material_id = Column(Integer, ForeignKey('materials.material_id'), nullable=True)
    check_in_date = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    employee = relationship('Employee', back_populates='checkins')
    tool = relationship('Tool', back_populates='checkins')
    material = relationship('Material', back_populates='checkins')


# CheckOut Table (Source Table for item_transactions)
class CheckOut(Base):
    __tablename__ = 'check_outs'
    check_out_id = Column(Integer, primary_key=True)  # Primary Key
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), nullable=True)
    material_id = Column(Integer, ForeignKey('materials.material_id'), nullable=True)
    check_out_date = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    employee = relationship('Employee', back_populates='checkouts')
    tool = relationship('Tool', back_populates='checkouts')
    material = relationship('Material', back_populates='checkouts')


# ItemInventory Table (Source Table for item_transactions / Front End Table)
class ItemInventory(Base):
    __tablename__ = 'item_inventory'
    item_id = Column(Integer, primary_key=True)  # This equates to either the material_id or the tool_id
    item_type = Column(String(50), nullable=False)  # 'tool' or 'material' - Specify length for VARCHAR
    item_stock = Column(Integer)
    item_out_of_stock_indicator = Column(Boolean)


# Transactions Table (Front End Table)
class Transactions(Base):
    __tablename__ = 'item_transactions'
    transaction_id = Column(Integer, primary_key=True)  # Primary Key
    transaction_owner_id = Column(Integer)  # Employee ID
    transaction_owner_name = Column(String(100))  # Specify length for VARCHAR
    transaction_item_id = Column(Integer)  # ID from item inventory
    transaction_type = Column(String(50))  # Tool Check Out, Tool Check In, Material Check Out, Material Check In - Specify length for VARCHAR
    transaction_status = Column(String(50))  # Open or Close - Specify length for VARCHAR
    transaction_open_date = Column(Date)
    transaction_close_date = Column(Date, nullable=True)  # Null if the check-out is ongoing