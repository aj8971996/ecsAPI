import uvicorn
from api.endpoints import app
from sqlalchemy import inspect, MetaData
from database.database import create_tables, seed_data, engine
from sqlalchemy.exc import OperationalError

def drop_tables_if_schema_changed(inspector, metadata):
    """
    Drops existing tables if the schema has changed.
    """
    try:
        # Reflect the existing database schema
        metadata.reflect(bind=engine)
        
        # Loop through each table in the metadata
        for table in metadata.tables.values():
            # Get the actual columns in the database table
            actual_columns = {col['name'] for col in inspector.get_columns(table.name)}
            
            # Get the columns defined in the SQLAlchemy model
            defined_columns = {col.name for col in table.columns}
            
            # If the columns differ, drop the table
            if actual_columns != defined_columns:
                print(f"Schema change detected for table '{table.name}'. Dropping table.")
                table.drop(bind=engine)
                
    except Exception as e:
        print(f"Error while checking for schema changes: {e}")
        raise e

def check_tables_and_seed_data():
    try:
        # Check if tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        metadata = MetaData()

        if tables:
            # Check if the schema has changed and drop tables if necessary
            drop_tables_if_schema_changed(inspector, metadata)

        # Recreate tables and seed data if necessary
        create_tables()

        if not tables or any(inspector.get_table_names()):
            # Tables were either just created or have been recreated due to schema changes
            seed_data()
            print("Tables created/recreated and sample data inserted successfully.")
        else:
            # Tables and data exist
            print("Tables and data already exist. API is running.")

    except OperationalError as e:
        print(f"Operational error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_tables_and_seed_data()
    uvicorn.run(app, host="0.0.0.0", port=8000)