# database/models.py (Using SQLAlchemy as ORM)
import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    #* Primary Key for Employee Table
    emp_id = Column(Integer, primary_key=True)
    #* Employee Information
    emp_first_name = Column(String)
    emp_last_name = Column(String)
    emp_job_title = Column(String)
    emp_start_date = Column(Date)
    #* Boolean indicator whether Employee has an active check-out
    emp_checkout_indicator = Column(Boolean, default=False)

class Tool(Base):
    __tablename__ = 'tools'
    #* Primary Key for Tools Table
    tool_id = Column(Integer, primary_key=True)
    #* Tool Information
    tool_name = Column(String)
    tool_type = Column(String)
    tool_added_to_inventory_date = Column(Date)
    tool_cost = Column(Float)
    tool_count = Column(Integer)
    #* Boolean indicator whether any amount of Tool is in inventory
    tool_out_of_stock_indicator = Column(Boolean, default=False)

class Material(Base):
    __tablename__ = 'materials'
    #* Primary Key for Material Table
    material_id = Column(Integer, primary_key=True)
    #* Material Information
    material_name = Column(String)
    material_type = Column(String)
    material_added_to_inventory_date = Column(Date)
    material_cost = Column(Float)
    material_count = Column(Integer)
    material_metric = Column(String)
    #* Boolean indicator whether any amount of Material is in inventory
    material_out_of_stock_indicator = Column(Boolean, default=False)

class CheckIn(Base):
    __tablename__ = 'check_ins'
    #* Primary Key for CheckIn Table
    check_in_id = Column(Integer, primary_key=True)
    #* Foreign Key to Employee
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))
    employee = relationship("Employee")
    #* Foreign Key to Tool
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), nullable=True)
    tool = relationship("Tool")
    #* Foreign Key to Material
    material_id = Column(Integer, ForeignKey('materials.material_id'), nullable=True)
    material = relationship("Material")
    #* Timestamp of Check-In
    check_in_date = Column(DateTime, default=datetime.datetime.utcnow)

class CheckOut(Base):
    __tablename__ = 'check_outs'
    #* Primary Key for CheckOut Table
    check_out_id = Column(Integer, primary_key=True)
    #* Foreign Key to Employee
    employee_id = Column(Integer, ForeignKey('employees.emp_id'))
    employee = relationship("Employee")
    #* Foreign Key to Tool
    tool_id = Column(Integer, ForeignKey('tools.tool_id'), nullable=True)
    tool = relationship("Tool")
    #* Foreign Key to Material
    material_id = Column(Integer, ForeignKey('materials.material_id'), nullable=True)
    material = relationship("Material")
    #* Timestamp of Check-Out
    check_out_date = Column(DateTime, default=datetime.datetime.utcnow)