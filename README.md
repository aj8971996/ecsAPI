README.md
@@ -0,0 +1,69 @@
# ecsAPI - Employee Checkout System API

## Overview

This repository contains the backend implementation of the ecsAPI, an Employee Checkout System designed for a 400-level college class. The API manages and tracks employee tool and material checkouts.

### Note

- The API is currently set up for development and testing purposes. It does not have a live server setup for running locally, nor does it include example data.
- The database and server configurations are set up for local development. To test the API, you will need to run it on a local server.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
### MySQL Setup
1. **Ensure MySQL Is Installed**
   
   Navigate to the MySQL Community Installer Page, ensure to install the connection tools AND a server instance

   https://dev.mysql.com/downloads/

   Recommended Downloads
   - MySQL Workbench
   - MySQL Community Server
   - Your relevant Connector(s)
### Environment Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aj8971996/ecsAPI.git
   cd ecsAPI

2. **Create and Activate a Virtual Enviornment**
    - On Windows
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
    - On macOS and Linus
        ```bash
        python3 -m venv venv
        source venv/bin/activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

### Running the API

1. **Start the API Server**

   - Navigate to the project's root directory if you are not already there:
     ```bash
     cd path/to/ecsAPI  # Replace 'path/to/ecsAPI' with the actual path in your local machine
     
   - Execute the following command to start the server:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000

   - This command starts the FastAPI server, making your API accessible at `http://localhost:8000` from any machine in the network.

2. **(IF FACING CONNECTION TO DB ISSUES) Test Your Database Connection**
   - Once MySQL Workbench is installed, you will need to create a local instance to test the connection with
   - Go into database.py and uncomment the following section
      ```bash
      """
      if __name__ == "__main__":
         try:
            get_db()
            print("Successfully connected to db")
         except Exception as e:
            print(f"Unable to get db : {e}")
      """
   - Then run the database.py file directly from your IDE to ensure you are connecting to your instance
   - The message you get should look like this
      ```bash
      c:/Users/17025/Desktop/dev_ecsAPI/ecsAPI/database/database.py
      Successfully connected to db
- To run the server in **reload mode** (useful during development as it automatically reloads your application when code changes are detected):
   ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000 --reload


This section provides the steps to start and interact with the API using Uvicorn, along with accessing its Swagger UI for easy testing and exploration of its capabilities.
