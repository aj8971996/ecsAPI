import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:8000";  // Replace with your FastAPI server URL

    public String validateEmployeeLogin(String username, String password) throws Exception {
        String endpoint = BASE_URL + "/login";
        String jsonInputString = "{\"username\": \"" + username + "\", \"password\": \"" + password + "\"}";
        return postResponse(endpoint, jsonInputString);
    }

    public String checkOutItem(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String endpoint = BASE_URL + "/checkout";
        String jsonInputString = "{\"employee_id\": " + employeeId + 
                                (toolId != null ? ", \"tool_id\": " + toolId : "") + 
                                (materialId != null ? ", \"material_id\": " + materialId + ", \"quantity\": " + quantity : "") + 
                                "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String checkInItem(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String endpoint = BASE_URL + "/checkin";
        String jsonInputString = "{\"employee_id\": " + employeeId + 
                                (toolId != null ? ", \"tool_id\": " + toolId : "") + 
                                (materialId != null ? ", \"material_id\": " + materialId + ", \"quantity\": " + quantity : "") + 
                                "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String getOutOfStockMaterials() throws Exception {
        String endpoint = BASE_URL + "/materials/out-of-stock";
        return getResponse(endpoint);
    }

    public String getLostTools() throws Exception {
        String endpoint = BASE_URL + "/tools/lost";
        return getResponse(endpoint);
    }

    public String getActiveCheckouts() throws Exception {
        String endpoint = BASE_URL + "/checkouts/active";
        return getResponse(endpoint);
    }

    private String getResponse(String endpoint) throws Exception {
        URL url = new URL(endpoint);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            return response.toString();
        } else {
            throw new Exception("GET request not worked, Response Code: " + responseCode);
        }
    }

    private String postResponse(String endpoint, String jsonInputString) throws Exception {
        URL url = new URL(endpoint);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json; utf-8");
        connection.setDoOutput(true);

        try(OutputStream os = connection.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);           
        }

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine.trim());
            }
            in.close();

            return response.toString();
        } else {
            throw new Exception("POST request not worked, Response Code: " + responseCode);
        }
    }

    public static void main(String[] args) {
        try {
            ApiClient apiClient = new ApiClient();
            
            // Example usage
            String loginResponse = apiClient.validateEmployeeLogin("johndoe", "password123");
            System.out.println("Login Response: " + loginResponse);

            String checkOutToolResponse = apiClient.checkOutItem(1, 2, null, 0);  // Check out tool (employeeId: 1, toolId: 2)
            System.out.println("Check Out Tool Response: " + checkOutToolResponse);

            String checkOutMaterialResponse = apiClient.checkOutItem(1, null, 3, 10);  // Check out material (employeeId: 1, materialId: 3, quantity: 10)
            System.out.println("Check Out Material Response: " + checkOutMaterialResponse);

            String checkInToolResponse = apiClient.checkInItem(1, 2, null, 0);  // Check in tool (employeeId: 1, toolId: 2)
            System.out.println("Check In Tool Response: " + checkInToolResponse);

            String checkInMaterialResponse = apiClient.checkInItem(1, null, 3, 10);  // Hypothetical return of material (employeeId: 1, materialId: 3, quantity: 10)
            System.out.println("Check In Material Response: " + checkInMaterialResponse);

            String outOfStockMaterials = apiClient.getOutOfStockMaterials();
            System.out.println("Out of Stock Materials: " + outOfStockMaterials);

            String lostTools = apiClient.getLostTools();
            System.out.println("Lost Tools: " + lostTools);

            String activeCheckouts = apiClient.getActiveCheckouts();
            System.out.println("Active Checkouts: " + activeCheckouts);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}