import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connectors.qdrant import QDrantConnector
from dotenv import load_dotenv

load_dotenv()
def test_qdrant():
    remote_endpoint = os.getenv("QDRANT_ENDPOINT_LOCAL")
    remote_api_key = os.getenv("QDRANT_API_KEY_LOCAL")
    connector = QDrantConnector(remote_endpoint, remote_api_key)

    #Health Check
    try:
        health = connector.health_check()
        print("Health Check passed successfully")
    except Exception as e:
        print("Health Check Failed: ", e)

    # # Test list collections
    # collections = connector.list_collections()
    # print("Collections:", collections)

if __name__ == "__main__":
    test_qdrant()