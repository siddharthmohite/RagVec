# In connectors/qdrant.py
import requests

class QDrantConnector:
    def __init__(self, endpoint: str, api_key: str = None):
        """
        Initializes the Qdrant connector.
        :param endpoint: The Qdrant API endpoint (e.g., "http://localhost:6333").
        :param api_key: API key for Qdrant (if applicable).
        """
        self.endpoint = endpoint
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

    def health_check(self):
        """
        Checks the health of the Qdrant server.
        :return: Response from the health check endpoint.
        """
        try:
            response = requests.get(f"{self.endpoint}/healthz", headers=self.headers)
            response.raise_for_status()
            # Check that the status is 200 and return True
            if response.status_code == 200:
                return True
            else:
               raise RuntimeError(f"Health check returned non 200 code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Health check failed: {e}")


    def get_metrics(self):
        """
        Gets the metrics from the Qdrant server.
        :return: Response from the metrics endpoint as JSON
        """
        try:
            response = requests.get(f"{self.endpoint}/metrics", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Metrics check failed: {e}")