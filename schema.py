# schemas.py
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

class EmployeeSchema(BaseModel):
    emp_id: int
    emp_first_name: str
    emp_last_name: str
    emp_job_title: Optional[str] = None
    emp_start_date: date
    emp_checkout_indicator: bool

    class Config:
        orm_mode = True

class ToolSchema(BaseModel):
    tool_id: int
    tool_name: str
    tool_type: Optional[str] = None
    tool_added_to_inventory_date: date
    tool_cost: Optional[float] = None
    tool_out_of_stock_indicator: bool
    tool_lost_indicator: bool

    class Config:
        orm_mode = True

class MaterialSchema(BaseModel):
    material_id: int
    material_name: str
    material_type: Optional[str] = None
    material_added_to_inventory_date: date
    material_cost: Optional[float] = None
    material_out_of_stock_indicator: bool
    material_lost_indicator: bool

    class Config:
        orm_mode = True

class CheckInOutSchema(BaseModel):
    transaction_id: int
    transaction_owner_id: int
    transaction_owner_name: str
    transaction_item_id: int
    transaction_type: str
    transaction_status: str
    transaction_open_date: date
    transaction_close_date: Optional[date] = None

    class Config:
        orm_mode = True

class InventorySchema(BaseModel):
    item_id: int
    item_type: str
    item_stock: int
    item_out_of_stock_indicator: bool
    item_lost_indicator: bool

    class Config:
        orm_mode = True
