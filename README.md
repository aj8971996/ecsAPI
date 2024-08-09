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

### Environment Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ecsAPI.git
   cd ecsAPI

2. **Create and Activate a Virtual Enviornment**
    - On Windows
        '''bash
        python -m venv venv
        .\venv\Scripts\activate
    - On macOS and Linus
        '''bash
        python3 -m venv venv
        source venv/bin/activate

3. **Install Dependencies**
    '''bash
    pip install -r requirements.txt

### Running the API

1. **Start the API Server**

   - Navigate to the project's root directory if you are not already there:
     ```bash
     cd path/to/ecsAPI  # Replace 'path/to/ecsAPI' with the actual path if necessary
     
   - Execute the following command to start the server:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000

   - This command starts the FastAPI server, making your API accessible at `http://localhost:8000` from any machine in the network.

2. **Accessing the API Documentation**

   - Once the server is running, open a web browser.
   - Visit `http://localhost:8000/docs` to view the Swagger UI. This page provides interactive API documentation, where you can test the API endpoints directly from your browser.

### Additional Server Commands

- To run the server in **reload mode** (useful during development as it automatically reloads your application when code changes are detected):
   ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000 --reload


This section provides the steps to start and interact with the API using Uvicorn, along with accessing its Swagger UI for easy testing and exploration of its capabilities.
