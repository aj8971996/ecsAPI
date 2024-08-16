# main.py
import uvicorn
from api.endpoints import app
from database.database import create_tables  # Import the function

# Create tables when the app starts
try:
    create_tables()
    print("All Tables Successfully Created in ecs_api schema")
except Exception as e:
    print(f"Tables Not Created with Error : {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)