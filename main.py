# main.py
import uvicorn
from api.endpoints import app
from database.database import create_tables  # Import the function

# Create tables when the app starts
create_tables()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)