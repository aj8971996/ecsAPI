import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:8000";  // Replace with your FastAPI server URL

    /**
     * Available Endpoints:
     * 
     * 1. POST /login
     *    - Function: loginEmployee
     *    - Description: Validates employee login credentials.
     * 
     * 2. POST /checkout
     *    - Function: checkoutItem
     *    - Description: Checks out a tool or material for an employee.
     * 
     * 3. POST /checkin
     *    - Function: checkinItem
     *    - Description: Checks in a tool or material for an employee.
     * 
     * 4. GET /materials/out-of-stock
     *    - Function: getOutOfStockMaterials
     *    - Description: Retrieves all out-of-stock materials.
     * 
     * 5. GET /tools/lost
     *    - Function: getLostTools
     *    - Description: Retrieves all lost tools.
     * 
     * 6. GET /checkouts/active
     *    - Function: getActiveCheckouts
     *    - Description: Retrieves all active checkouts.
     * 
     * 7. GET /inventory
     *    - Function: getInventory
     *    - Description: Retrieves the full inventory of tools and materials.
     * 
     * 8. POST /tools/lost/{tool_id}
     *    - Function: reportLostTool
     *    - Description: Reports a checked-out tool as lost.
     */

    public String loginEmployee(String username, String password) throws Exception {
        String endpoint = BASE_URL + "/login";
        String jsonInputString = "{\"username\": \"" + username + "\", \"password\": \"" + password + "\"}";
        return postResponse(endpoint, jsonInputString);
    }

    public Map<String, Object> loginEmployeeParsed(String username, String password) throws Exception {
        String jsonResponse = loginEmployee(username, password);
        return parseJsonResponse(jsonResponse);
    }

    public String checkoutItem(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String endpoint = BASE_URL + "/checkout";
        String jsonInputString = "{\"employee_id\": " + employeeId +
                                (toolId != null ? ", \"tool_id\": " + toolId : "") +
                                (materialId != null ? ", \"material_id\": " + materialId + ", \"quantity\": " + quantity : "") +
                                "}";
        return postResponse(endpoint, jsonInputString);
    }

    public Map<String, Object> checkoutItemParsed(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String jsonResponse = checkoutItem(employeeId, toolId, materialId, quantity);
        return parseJsonResponse(jsonResponse);
    }

    public String checkinItem(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String endpoint = BASE_URL + "/checkin";
        String jsonInputString = "{\"employee_id\": " + employeeId +
                                (toolId != null ? ", \"tool_id\": " + toolId : "") +
                                (materialId != null ? ", \"material_id\": " + materialId + ", \"quantity\": " + quantity : "") +
                                "}";
        return postResponse(endpoint, jsonInputString);
    }

    public Map<String, Object> checkinItemParsed(int employeeId, Integer toolId, Integer materialId, int quantity) throws Exception {
        String jsonResponse = checkinItem(employeeId, toolId, materialId, quantity);
        return parseJsonResponse(jsonResponse);
    }

    public String getOutOfStockMaterials() throws Exception {
        String endpoint = BASE_URL + "/materials/out-of-stock";
        return getResponse(endpoint);
    }

    public Map<String, Object> getOutOfStockMaterialsParsed() throws Exception {
        String jsonResponse = getOutOfStockMaterials();
        return parseJsonResponse(jsonResponse);
    }

    public String getLostTools() throws Exception {
        String endpoint = BASE_URL + "/tools/lost";
        return getResponse(endpoint);
    }

    public Map<String, Object> getLostToolsParsed() throws Exception {
        String jsonResponse = getLostTools();
        return parseJsonResponse(jsonResponse);
    }

    public String getActiveCheckouts() throws Exception {
        String endpoint = BASE_URL + "/checkouts/active";
        return getResponse(endpoint);
    }

    public Map<String, Object> getActiveCheckoutsParsed() throws Exception {
        String jsonResponse = getActiveCheckouts();
        return parseJsonResponse(jsonResponse);
    }

    public String getInventory() throws Exception {
        String endpoint = BASE_URL + "/inventory";
        return getResponse(endpoint);
    }

    public Map<String, Object> getInventoryParsed() throws Exception {
        String jsonResponse = getInventory();
        return parseJsonResponse(jsonResponse);
    }

    // New function to report a lost tool
    public String reportLostTool(int toolId) throws Exception {
        String endpoint = BASE_URL + "/tools/lost/" + toolId;
        return postResponse(endpoint, "");
    }

    public Map<String, Object> reportLostToolParsed(int toolId) throws Exception {
        String jsonResponse = reportLostTool(toolId);
        return parseJsonResponse(jsonResponse);
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

    private Map<String, Object> parseJsonResponse(String jsonResponse) {
        JSONObject jsonObject = new JSONObject(jsonResponse);
        Map<String, Object> resultMap = new HashMap<>();

        for (String key : jsonObject.keySet()) {
            Object value = jsonObject.get(key);
            resultMap.put(key, value);
        }

        return resultMap;
    }
}