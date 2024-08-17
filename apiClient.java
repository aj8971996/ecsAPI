import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:8000";  // Replace with your FastAPI server URL

    public String validateEmployeeLogin(String username, String password) throws Exception {
        String endpoint = BASE_URL + "/validate-login";
        String jsonInputString = "{\"username\": \"" + username + "\", \"password\": \"" + password + "\"}";
        return postResponse(endpoint, jsonInputString);
    }

    public String getInventory() throws Exception {
        String endpoint = BASE_URL + "/inventory";
        return getResponse(endpoint);
    }

    public String checkOutTool(int employeeId, int toolId) throws Exception {
        String endpoint = BASE_URL + "/check-out";
        String jsonInputString = "{\"employee_id\": " + employeeId + ", \"tool_id\": " + toolId + "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String checkInTool(int employeeId, int toolId) throws Exception {
        String endpoint = BASE_URL + "/check-in";
        String jsonInputString = "{\"employee_id\": " + employeeId + ", \"tool_id\": " + toolId + "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String getActiveCheckouts() throws Exception {
        String endpoint = BASE_URL + "/active-checkouts";
        return getResponse(endpoint);
    }

    public String getActiveLostItems() throws Exception {
        String endpoint = BASE_URL + "/active-lost-items";
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

            String inventory = apiClient.getInventory();
            System.out.println("Inventory: " + inventory);

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
}