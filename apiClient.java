import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:8000";  // Replace with your FastAPI server URL

    public String getEmployees() throws Exception {
        String endpoint = BASE_URL + "/employees";
        return getResponse(endpoint);
    }

    public String getInventory() throws Exception {
        String endpoint = BASE_URL + "/inventory";
        return getResponse(endpoint);
    }

    public String getOpenTransactions() throws Exception {
        String endpoint = BASE_URL + "/open-transactions";
        return getResponse(endpoint);
    }

    public String getActiveCheckouts() throws Exception {
        String endpoint = BASE_URL + "/active-checkouts";
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

    public static void main(String[] args) {
        try {
            ApiClient apiClient = new ApiClient();
            String employees = apiClient.getEmployees();
            System.out.println("Employees: " + employees);

            String inventory = apiClient.getInventory();
            System.out.println("Inventory: " + inventory);

            String openTransactions = apiClient.getOpenTransactions();
            System.out.println("Open Transactions: " + openTransactions);

            String activeCheckouts = apiClient.getActiveCheckouts();
            System.out.println("Active Checkouts: " + activeCheckouts);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
