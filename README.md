README.md
@@ -0,0 +1,69 @@
# ecsAPI - Employee Checkout System API

## Overview

This repository contains the backend implementation of the ecsAPI, an Employee Checkout System designed for a 400-level college class. The API manages and tracks employee tool and material checkouts.

### Note

- The API is currently set up for development and testing purposes. It does not have a live server setup and is intended to run locally. Additionally, no example data is included.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- MySQL

### MySQL Setup
1. **Ensure MySQL Is Installed**
   
   Navigate to the MySQL Community Installer Page and install the connection tools along with a server instance.


   https://dev.mysql.com/downloads/

   Recommended Downloads
   - MySQL Workbench
   - MySQL Community Server
   - Your relevant Connector(s)

2. **Ensure ECS API User is Created**

   The connection to the API requires that the ECS API user is created and privileges are granted.

   Please follow these steps:
   1. *Creaet the User*
      ```bash
      CREATE USER 'ecs_api_user'@'localhost' IDENTIFIED BY 'password';
      ```
   2. *Grant the Privileges*
      ```bash
      GRANT ALL PRIVILEGES ON ecs_api.*TO'ecs_api_user'@'localhost';
      ```
   3. *Commit the Change*
      ```bash
      FLUSH PRIVILEGES;
      ```

### Environment Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aj8971996/ecsAPI.git
   cd ecsAPI
   ```

2. **Create and Activate a Virtual Enviornment**
    - On Windows
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - On macOS and Linus
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1. **Start the API Server**

   - Navigate to the project's root directory if you are not already there:
     ```bash
     cd path/to/ecsAPI  # Replace 'path/to/ecsAPI' with the actual path in your local machine
     ```
     
   - Execute the following command to start the server:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

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
      ```
   - Then run the database.py file directly from your IDE to ensure you are connecting to your instance
   - The message you get should look like this
      ```bash
      Successfully connected to db
      ```

This section provides the steps to start and interact with the API using Uvicorn, along with accessing its Swagger UI for easy testing and exploration of its capabilities.

### API Client Usage
   The apiClient.java class provides several methods to interact with the backend API. Below are the available methods:

### Validate Employee Login
   ```java
   String loginResponse = apiClient.validateEmployeeLogin("johndoe", "password123");
   System.out.println("Login Response: " + loginResponse);
   ```

### Retrieve Employees
   ```java
   String employees = apiClient.getEmployees();
   System.out.println("Employees: " + employees);
   ```

### Retrieve Inventory
   ```java
   String inventory = apiClient.getInventory();
   System.out.println("Inventory: " + inventory);
   ```

### Retrieve Open Transactions
   ```java
   String openTransactions = apiClient.getOpenTransactions();
   System.out.println("Open Transactions: " + openTransactions);
   ```

### Check Out Tool
   ```java
   String checkOutResponse = apiClient.checkOutTool(1, 2);  // Example employee ID and tool ID
   System.out.println("Check Out Response: " + checkOutResponse);
   ```

### Check In Tool
   ```java
   String checkInResponse = apiClient.checkInTool(1, 2);  // Example employee ID and tool ID
   System.out.println("Check In Response: " + checkInResponse);
   ```

### Retrieve Active Checkouts
   ```java
   String activeCheckouts = apiClient.getActiveCheckouts();
   System.out.println("Active Checkouts: " + activeCheckouts);
   ```

### Retrieve Active Lost Items
   ```java
   String activeLostItems = apiClient.getActiveLostItems();
   System.out.println("Active Lost Items: " + activeLostItems);
   ```

### Example Usage for Main method in Java
```java
public static void main(String[] args) {
    try {
        ApiClient apiClient = new ApiClient();
        String employees = apiClient.getEmployees();
        System.out.println("Employees: " + employees);

        // Example usage
        String loginResponse = apiClient.validateEmployeeLogin("johndoe", "password123");
        System.out.println("Login Response: " + loginResponse);

        String inventory = apiClient.getInventory();
        System.out.println("Inventory: " + inventory);

        String openTransactions = apiClient.getOpenTransactions();
        System.out.println("Open Transactions: " + openTransactions);

        String checkOutResponse = apiClient.checkOutTool(1, 2);  // Example employee ID and tool ID
        System.out.println("Check Out Response: " + checkOutResponse);

        String checkInResponse = apiClient.checkInTool(1, 2);  // Example employee ID and tool ID
        System.out.println("Check In Response: " + checkInResponse);

        String activeCheckouts = apiClient.getActiveCheckouts();
        System.out.println("Active Checkouts: " + activeCheckouts);

        String activeLostItems = apiClient.getActiveLostItems();
        System.out.println("Active Lost Items: " + activeLostItems);

    } catch (Exception e) {
        e.printStackTrace();
    }
}
```