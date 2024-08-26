import uvicorn
from api.endpoints import app
from sqlalchemy import inspect
from database.database import create_tables, seed_data, engine
from sqlalchemy.exc import OperationalError

def check_tables_and_seed_data():
    try:
        # Check if tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        if not tables:
            # No tables exist, create tables and seed data
            create_tables()
            seed_data()
            print("Tables created and sample data inserted successfully.")
        else:
            # Tables exist, check if data is present
            with engine.connect() as connection:
                data_present = False
                for table_name in tables:
                    result = connection.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
                    if result.fetchone() is not None:
                        data_present = True
                        break

                if not data_present:
                    # Tables exist but no data, seed the data
                    seed_data()
                    print("Sample data inserted successfully.")
                else:
                    # Tables and data exist, check if schema matches
                    # (For simplicity, assuming schema matches if tables exist and have data)
                    print("Tables and data already exist. API is running.")

    except OperationalError as e:
        print(f"Operational error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_tables_and_seed_data()
    uvicorn.run(app, host="0.0.0.0", port=8000)