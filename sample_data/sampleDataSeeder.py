import datetime
from sqlalchemy.orm import Session
from database.models import Employee, Tool, Material, Transactions, RefillRequest

class SampleDataSeeder:
    def __init__(self, db: Session):
        self.db = db

    def seed(self):
        try:
            self._seed_employees()
            self._seed_tools()
            self._seed_materials()
            self._seed_transactions()  # Seeding transactions
            self._seed_refill_requests()  # Seeding refill requests
            self.db.commit()
            print("Data seeding completed successfully.")
        except Exception as e:
            print(f"An error occurred during seeding: {e}")
            self.db.rollback()  # Rollback in case of error

    def _seed_employees(self):
        try:
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
            self.db.commit()  # Commit after seeding employees
            print(f"Seeded {len(employees)} employees successfully.")
        except Exception as e:
            print(f"Failed to seed employees: {e}")
            self.db.rollback()

    def _seed_tools(self):
        try:
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
            self.db.commit()  # Commit after seeding tools
            print(f"Seeded {len(tools)} tools successfully.")
        except Exception as e:
            print(f"Failed to seed tools: {e}")
            self.db.rollback()

    def _seed_materials(self):
        try:
            materials = [
                Material(
                    material_name="Wood Plank",
                    material_type="Building Material",
                    material_added_to_inventory_date=datetime.date(2022, 1, 25),
                    material_cost=5.0,
                    material_metric="Piece",
                    material_quantity_available=100,
                    material_out_of_stock_indicator=False
                ),
                Material(
                    material_name="Nails",
                    material_type="Fastener",
                    material_added_to_inventory_date=datetime.date(2022, 2, 18),
                    material_cost=0.02,
                    material_metric="Count",
                    material_quantity_available=10000,
                    material_out_of_stock_indicator=False
                ),
                Material(
                    material_name="Copper Wire",
                    material_type="Electrical",
                    material_added_to_inventory_date=datetime.date(2022, 3, 20),
                    material_cost=1.5,
                    material_metric="Meter",
                    material_quantity_available=500,
                    material_out_of_stock_indicator=False
                ),
            ]
            self.db.add_all(materials)
            self.db.commit()  # Commit after seeding materials
            print(f"Seeded {len(materials)} materials successfully.")
        except Exception as e:
            print(f"Failed to seed materials: {e}")
            self.db.rollback()

    def _seed_transactions(self):
        try:
            transactions = [
                Transactions(
                    transaction_owner_id=1,  # John Doe
                    transaction_owner_name="John Doe",
                    transaction_item_id=1,  # Hammer (Tool)
                    transaction_type="Tool Check Out",
                    transaction_status="Open",
                    transaction_open_date=datetime.date(2022, 5, 1)
                ),
                Transactions(
                    transaction_owner_id=2,  # Jane Smith
                    transaction_owner_name="Jane Smith",
                    transaction_item_id=2,  # Nails (Material)
                    transaction_type="Material Issued",
                    transaction_status="Closed",
                    transaction_quantity=500,
                    transaction_open_date=datetime.date(2022, 6, 15),
                    transaction_close_date=datetime.date(2022, 6, 20)
                ),
            ]
            self.db.add_all(transactions)
            self.db.commit()  # Commit after seeding transactions
            print(f"Seeded {len(transactions)} transactions successfully.")
        except Exception as e:
            print(f"Failed to seed transactions: {e}")
            self.db.rollback()

    def _seed_refill_requests(self):
        try:
            refill_requests = [
                RefillRequest(
                    employee_id=1,  # John Doe
                    item_id=1,  # Hammer (Tool)
                    request_type="lost",
                    request_status="Pending",
                    request_date=datetime.datetime.utcnow()
                ),
                RefillRequest(
                    employee_id=2,  # Jane Smith
                    item_id=3,  # Copper Wire (Material)
                    request_type="out_of_stock",
                    request_status="Approved",
                    request_date=datetime.datetime.utcnow()
                ),
            ]
            self.db.add_all(refill_requests)
            self.db.commit()  # Commit after seeding refill requests
            print(f"Seeded {len(refill_requests)} refill requests successfully.")
        except Exception as e:
            print(f"Failed to seed refill requests: {e}")
            self.db.rollback()

# Usage example:
# from sqlalchemy.orm import Session
# from database.sample_data_seeder import SampleDataSeeder

# def create_sample_data(db: Session):
#     seeder = SampleDataSeeder(db)
#     seeder.seed()