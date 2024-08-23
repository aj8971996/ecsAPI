# database/sample_data_seeder.py
import datetime
from sqlalchemy.orm import Session
from database.models import Employee, Tool, Material, CheckOut, CheckIn

class SampleDataSeeder:
    def __init__(self, db: Session):
        self.db = db

    def seed(self):
        self._seed_employees()
        self._seed_tools()
        self._seed_materials()
        self.db.commit()

    def _seed_employees(self):
        employees = [
            Employee(
                emp_first_name="John",
                emp_last_name="Doe",
                emp_job_title="Technician",
                emp_start_date=datetime.date(2021, 5, 1),
                emp_checkout_indicator=False,
                emp_user_name="jdoe",
                emp_password="password123"
            ),
            Employee(
                emp_first_name="Jane",
                emp_last_name="Smith",
                emp_job_title="Engineer",
                emp_start_date=datetime.date(2020, 6, 15),
                emp_checkout_indicator=False,
                emp_user_name="jsmith",
                emp_password="password456"
            ),
            Employee(
                emp_first_name="Alice",
                emp_last_name="Johnson",
                emp_job_title="Manager",
                emp_start_date=datetime.date(2019, 3, 22),
                emp_checkout_indicator=False,
                emp_user_name="ajohnson",
                emp_password="password789"
            ),
        ]
        self.db.add_all(employees)

    def _seed_tools(self):
        tools = [
            Tool(
                tool_name="Hammer",
                tool_type="Hand Tool",
                tool_added_to_inventory_date=datetime.date(2022, 1, 10),
                tool_cost=20.0,
                tool_lost_indicator=False,
                tool_out_of_stock_indicator=False
            ),
            Tool(
                tool_name="Screwdriver",
                tool_type="Hand Tool",
                tool_added_to_inventory_date=datetime.date(2022, 2, 5),
                tool_cost=10.0,
                tool_lost_indicator=False,
                tool_out_of_stock_indicator=False
            ),
            Tool(
                tool_name="Drill",
                tool_type="Power Tool",
                tool_added_to_inventory_date=datetime.date(2022, 3, 15),
                tool_cost=150.0,
                tool_lost_indicator=False,
                tool_out_of_stock_indicator=False
            ),
            Tool(
                tool_name="Wrench",
                tool_type="Hand Tool",
                tool_added_to_inventory_date=datetime.date(2022, 4, 12),
                tool_cost=15.0,
                tool_lost_indicator=False,
                tool_out_of_stock_indicator=False
            ),
        ]
        self.db.add_all(tools)

    def _seed_materials(self):
        materials = [
            Material(
                material_name="Wood Plank",
                material_type="Building Material",
                material_added_to_inventory_date=datetime.date(2022, 1, 25),
                material_cost=5.0,
                material_out_of_stock_indicator=False
            ),
            Material(
                material_name="Nails",
                material_type="Fastener",
                material_added_to_inventory_date=datetime.date(2022, 2, 18),
                material_cost=0.02,
                material_out_of_stock_indicator=False
            ),
            Material(
                material_name="Copper Wire",
                material_type="Electrical",
                material_added_to_inventory_date=datetime.date(2022, 3, 20),
                material_cost=1.5,
                material_out_of_stock_indicator=False
            ),
        ]
        self.db.add_all(materials)

# Usage example:
# from sqlalchemy.orm import Session
# from database.sample_data_seeder import SampleDataSeeder

# def create_sample_data(db: Session):
#     seeder = SampleDataSeeder(db)
#     seeder.seed()
