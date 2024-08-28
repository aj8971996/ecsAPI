# ecsAPI - Employee Checkout System API

## Overview

This repository contains the backend implementation of the `ecsAPI`, an Employee Checkout System developed for a 400-level college class. The API is designed to manage and track employee checkouts for tools and materials.

### Key Features:
- **Automatic Table and Data Management:** The API automatically checks if the necessary tables exist and if they contain data:
  - If tables do not exist, they will be created, and sample data will be seeded.
  - If tables exist but are empty, only the sample data will be seeded.
  - If tables and data already exist, the API confirms that it is running correctly without duplicating data or tables.
- **Tool Management:** Ability to add new tools to the inventory and mark lost tools as replaced.
- **Seamless Integration:** The API interacts with MySQL for backend data storage, ensuring reliable and scalable database management.

### Note
- **Development and Testing:** This API is set up for local development and testing purposes. It does not include a live server setup.
- **Sample Data:** The `sampleDataSeeder.py` script located in the `sample_data` subfolder handles the seeding of sample data into the database. This sample data is automatically inserted into the tables upon creation, or if the tables exist but are empty.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- **Python 3.8 or higher**: Required for running the FastAPI application and other Python scripts.
- **pip (Python package installer)**: Needed for installing dependencies.
- **MySQL**: A MySQL instance is required for the API’s database operations.

### MySQL Setup
1. **Install MySQL**

   Visit the MySQL Community Installer page to download and install the necessary tools, including MySQL Workbench and MySQL Community Server.

   [MySQL Downloads](https://dev.mysql.com/downloads/)

   **Recommended Downloads:**
   - **MySQL Workbench**: For database management and queries.
   - **MySQL Community Server**: The MySQL server instance.
   - **MySQL Connector(s)**: For connecting applications to the MySQL server.

2. **Create the ECS API User**

   The API requires a specific MySQL user with the necessary privileges. Follow the steps below to create the user:

   1. **Create the User**
      ```sql
      CREATE USER 'ecs_api_user'@'localhost' IDENTIFIED BY 'password';
      ```
   2. **Grant Privileges**
      ```sql
      GRANT ALL PRIVILEGES ON ecs_api.* TO 'ecs_api_user'@'localhost';
      ```
   3. **Commit the Changes**
      ```sql
      FLUSH PRIVILEGES;
      ```

### Environment Setup

1. **Clone the Repository**

   Begin by cloning the ecsAPI repository to your local machine:

   ```bash
   git clone https://github.com/aj8971996/ecsAPI.git
   cd ecsAPI
   ```

2. **Create and Activate a Virtual Environment**

   Setting up a virtual environment ensures that your dependencies are isolated from other projects:

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

   With the virtual environment activated, install all necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API

1. **Start the API Server**
   - Ensure you're in the root directory of the project:
     ```bash
     cd path/to/ecsAPI  # Replace 'path/to/ecsAPI' with the actual path on your local machine
     ```
   - Start the FastAPI server by running:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```
   - This command makes the API accessible at `http://localhost:8000` from any machine on your network.

2. **Database Setup and Management**
   - Upon startup, the API checks the MySQL database for the necessary tables:
     - **Table Creation & Data Seeding:** If the tables do not exist, the API creates them and seeds them with sample data.
     - **Data Seeding Only:** If the tables exist but are empty, only the sample data is seeded.
     - **Running Status Confirmation:** If the tables exist and contain data, and the schema is up to date, the API confirms that it is running correctly.
   - No manual intervention is required unless an issue arises. Logs will provide detailed information on the actions taken.

3. **Troubleshooting Database Connection Issues**
   - If you're facing issues connecting to the database, use MySQL Workbench to create a local instance for testing.
   - In the `database.py` file, uncomment the following section to test the connection:
     ```python
     """
     if __name__ == "__main__":
        try:
           get_db()
           print("Successfully connected to db")
        except Exception as e:
           print(f"Unable to get db : {e}")
     """
     ```
   - Run `database.py` directly from your IDE. If successful, you should see:
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
   
   - Validates an Employee Login

2. **Retrieve Employees**
   ```java
   String employees = apiClient.getEmployees();
   System.out.println("Employees: " + employees);
   ```

   - Retrieves all Employees

3. **Retrieve Inventory**
   ```java
   String inventory = apiClient.getInventory();
   System.out.println("Inventory: " + inventory);
   ```

   - Retrieves Inventory of All Items

4. **Retrieve Open Transactions**
   ```java
   String openTransactions = apiClient.getActiveCheckouts();
   System.out.println("Open Transactions: " + openTransactions);
   ```

   - Retrieve Open Transactions

5. **Check Out Tool or Material**
   ```java
   String checkOutToolResponse = apiClient.checkoutItem(1, 2, null, 0);  // Check out tool (employeeId: 1, toolId: 2)
   System.out.println("Check Out Tool Response: " + checkOutToolResponse);

   String checkOutMaterialResponse = apiClient.checkoutItem(1, null, 3, 10);  // Check out material (employeeId: 1, materialId: 3, quantity: 10)
   System.out.println("Check Out Material Response: " + checkOutMaterialResponse);
   ```

   - Check Out a Tool or Materal - providing an Employee ID and Tool ID, or Material ID AND Quantity

6. **Check In Tool or Material**
   ```java
   String checkInToolResponse = apiClient.checkinItem(1, 2, null, 0);  // Check in tool (employeeId: 1, toolId: 2)
   System.out.println("Check In Tool Response: " + checkInToolResponse);

   String checkInMaterialResponse = apiClient.checkinItem(1, null, 3, 10);  // Hypothetical return of material (employeeId: 1, materialId: 3, quantity: 10)
   System.out.println("Check In Material Response: " + checkInMaterialResponse);
   ```

   - Check In a Tool or Materal - providing an Employee ID and Tool ID, or Material ID AND Quantity

7. **Retrieve Out of Stock Materials**
   ```java
   String outOfStockMaterials = apiClient.getOutOfStockMaterials();
   System.out.println("Out of Stock Materials: " + outOfStockMaterials);
   ```

   - Retrieve the Out of Stock Materials

8. **Retrieve Lost Tools**
   ```java
   String lostTools = apiClient.getLostTools();
   System.out.println("Lost Tools: " + lostTools);
   ```

   - Retrieve the Lost Tools

9. **Report Lost Tool**
   ```java
   String lostToolResponse = apiClient.reportLostTool(2);  // Mark tool with ID 2 as lost
   System.out.println("Lost Tool Response: " + lostToolResponse);
   ```

   - Report a Tool as Lost

10. **[New] Submit Refill Request**
   ```java
   String refillResponse = apiClient.requestRefill(1, 3, "out_of_stock");  // Request refill for material (employeeId: 1, materialId: 3)
   System.out.println("Refill Request Response: " + refillResponse);
   ```

   - Submit a Request to Refill an Item

11. **[New] Retrieve all Refill Requests**
   ```Java
   String refillRequests = apiClient.getRefillRequests();
   System.out.println("Refill Requests: " + refillRequests);
   ```

   - View all Refill Requests

12. **[New] Add New Tool**
   ```java
   String addToolResponse = apiClient.addNewTool("Hammer", "Hand Tool", 19.99);
   System.out.println("Add Tool Response: " + addToolResponse);
   ```

   - Add new Tool to database

13. **[New] Mark Tool as Replaced**
   ```java
   String replaceToolResponse = apiClient.markToolAsReplaced(2);  // Replace tool with ID 2
   System.out.println("Replace Tool Response: " + replaceToolResponse);
   ```

   - Mark a Tool as Replaced, this sets the lost indicator back to 0. 
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