from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base  # Use absolute path for import
from sample_data.sampleDataSeeder import SampleDataSeeder  # Absolute path for import

# Use pymysql in the connection string
DATABASE_URL = "mysql+pymysql://ecs_api_user:password@localhost/ecs_api"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

def seed_data():
    with SessionLocal() as db:
        seeder = SampleDataSeeder(db)
        seeder.seed()
        print("Sample data successfully inserted.")

# Test connection and seed data
if __name__ == "__main__":
    try:
        create_tables()
        seed_data()
        print("Tables created and sample data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")