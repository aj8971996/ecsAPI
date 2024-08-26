# ecsAPI - Employee Checkout System API

## Overview

This repository contains the backend implementation of the ecsAPI, an Employee Checkout System designed for a 400-level college class. The API manages and tracks employee tool and material checkouts.

- The API now includes logic to check if the tables exist and if they contain data. If tables do not exist, they will be created and seeded with sample data. If the tables exist but are empty, only the data will be seeded. If both tables and data exist, the API will inform that it is running correctly.

### Note

- The API is currently set up for development and testing purposes. It does not have a live server setup. This is intended to run locally.
- Sample data is now included within the `sampleDataSeeder.py` class located within the `sample_data` subfolder.
  - The sample data is inserted into the tables upon table creation, or if the tables exist but are empty.

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

   Recommended Downloads:
   - MySQL Workbench
   - MySQL Community Server
   - Your relevant Connector(s)

2. **Ensure ECS API User is Created**

   The connection to the API requires that the ECS API user is created and privileges are granted.

   Please follow these steps:
   1. *Create the User*
      ```sql
      CREATE USER 'ecs_api_user'@'localhost' IDENTIFIED BY 'password';
      ```
   2. *Grant the Privileges*
      ```sql
      GRANT ALL PRIVILEGES ON ecs_api.* TO 'ecs_api_user'@'localhost';
      ```
   3. *Commit the Change*
      ```sql
      FLUSH PRIVILEGES;
      ```

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
   - Execute the following command to start the server
      ```bash
      uvicorn main:app --host 0.0.0.0 --port 8000
      ```
   - This command starts the FastAPI server, making your API accessible at `http://localhost:8000` from any machine in the network.

2. **Database Setup and Management**
   - The API automatically checks if the necessary tables exist in the MySQL database when it starts. Depending on the state of the database, it will:
      - Create tables and seed data: If the tables do not exist, the API will create them and insert sample data automatically.
      - Seed data only: If the tables exist but are empty, the API will insert the sample data without altering the schema.
      - Confirm running status: If the tables exist and contain data, and the schema matches the current version, the API will simply confirm that everything is running correctly.
   - No manual intervention is needed unless there's an issue. The log output will inform you of the actions taken during startup.

3. **(IF FACING CONNECTION TO DB ISSUES) Test Your Database Connection**
   - Once MySQL Workbench is installed, you will need to create a local instance to test the connection with.
   - Go into database.py and uncomment the following section:
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
   - Then run the database.py file directly from your IDE to ensure you are connecting to your instance.
   - The message you get should look like this:
      ```bash
      Successfully connected to db
      ```

### API Endpoints and Client Usage
The apiClient.java class provides several methods to interact with the backend API. Below are the available methods:
1. **Validate Employee Login**
   ```java
   String loginResponse = apiClient.loginEmployee("johndoe", "password123");
   System.out.println("Login Response: " + loginResponse);
   ```
2. **Retrieve Employees**
   ```java
   String employees = apiClient.getEmployees();
   System.out.println("Employees: " + employees);
   ```
3. **Retrieve Inventory**
   ```java
   String inventory = apiClient.getInventory();
   System.out.println("Inventory: " + inventory);
   ```
4. **Retrieve Open Transactions**
   ```java
   String openTransactions = apiClient.getActiveCheckouts();
   System.out.println("Open Transactions: " + openTransactions);
   ```
5. **Check Out Tool or Material**
   ```java
   String checkOutToolResponse = apiClient.checkoutItem(1, 2, null, 0);  // Check out tool (employeeId: 1, toolId: 2)
   System.out.println("Check Out Tool Response: " + checkOutToolResponse);

   String checkOutMaterialResponse = apiClient.checkoutItem(1, null, 3, 10);  // Check out material (employeeId: 1, materialId: 3, quantity: 10)
   System.out.println("Check Out Material Response: " + checkOutMaterialResponse);
   ```
6. **Check In Tool or Material**
   ```java
   String checkInToolResponse = apiClient.checkinItem(1, 2, null, 0);  // Check in tool (employeeId: 1, toolId: 2)
   System.out.println("Check In Tool Response: " + checkInToolResponse);

   String checkInMaterialResponse = apiClient.checkinItem(1, null, 3, 10);  // Hypothetical return of material (employeeId: 1, materialId: 3, quantity: 10)
   System.out.println("Check In Material Response: " + checkInMaterialResponse);
   ```
7. **Retrieve Out of Stock Materials**
   ```java
   String outOfStockMaterials = apiClient.getOutOfStockMaterials();
   System.out.println("Out of Stock Materials: " + outOfStockMaterials);
   ```
8. **Retrieve Lost Tools**
   ```java
   String lostTools = apiClient.getLostTools();
   System.out.println("Lost Tools: " + lostTools);
   ```
9. **Report Lost Tool**
   ```java
   String lostToolResponse = apiClient.reportLostTool(2);  // Mark tool with ID 2 as lost
   System.out.println("Lost Tool Response: " + lostToolResponse);
   ```
**Example Usage in Main Method**
```java
public static void main(String[] args) {
    try {
        ApiClient apiClient = new ApiClient();

        // Example usage
        String loginResponse = apiClient.loginEmployee("johndoe", "password123");
        System.out.println("Login Response: " + loginResponse);

        String checkOutToolResponse = apiClient.checkoutItem(1, 2, null, 0);  // Check out tool (employeeId: 1, toolId: 2)
        System.out.println("Check Out Tool Response: " + checkOutToolResponse);

        String checkOutMaterialResponse = apiClient.checkoutItem(1, null, 3, 10);  // Check out material (employeeId: 1, materialId: 3, quantity: 10)
        System.out.println("Check Out Material Response: " + checkOutMaterialResponse);

        String checkInToolResponse = apiClient.checkinItem(1, 2, null, 0);  // Check in tool (employeeId: 1, toolId: 2)
        System.out.println("Check In Tool Response: " + checkInToolResponse);

        String checkInMaterialResponse = apiClient.checkinItem(1, null, 3, 10);  // Hypothetical return of material (employeeId: 1, materialId: 3, quantity: 10)
        System.out.println("Check In Material Response: " + checkInMaterialResponse);

        String activeCheckouts = apiClient.getActiveCheckouts();
        System.out.println("Active Checkouts: " + activeCheckouts);

        String lostTools = apiClient.getLostTools();
        System.out.println("Lost Tools: " + lostTools);

    } catch (Exception e) {
        e.printStackTrace();
    }
}
```
### Final Notes
- Troubleshooting tips are provided in the respective sections above. If issues persist, consider checking MySQL connection settings or reviewing the API logs for detailed error messages.