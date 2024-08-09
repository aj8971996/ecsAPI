from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from .models import Base

# Create the engine with the appropriate database URL
engine = create_engine('sqlite:///employee_checkout.db', echo=True)  # Adjust the URL as necessary

# Create all tables in the database from the defined models
Base.metadata.create_all(engine)

# Create a sessionmaker bound to this engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Database:
    @staticmethod
    def get_db():
        """Yield database sessions, ensuring they are closed after use."""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
