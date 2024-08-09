#! PLACEHOLDER - IN PROGRESS
# main.py
import uvicorn
from api.endpoints import app  # Ensure this path matches your project structure

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run your server at 0.0.0.0:8000