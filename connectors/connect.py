# connectors/connect.py
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from pinecone import Pinecone

load_dotenv()  # Load environment variables

def connection(db_type: str, **kwargs):
    """
    Creates a connection to either Pinecone or Qdrant, based on the db_type.
    :param db_type: "pinecone" or "qdrant"
    :return: Connection object
    """
    if db_type.lower() == "pinecone":
        # Fetch api key here from environment variables
        pinecone_api_key = os.getenv("PINECONE_API_KEY_REMOTE")
        if not pinecone_api_key:
            raise ValueError("Pinecone API key must be provided")

        try:
            connector = Pinecone(api_key=pinecone_api_key)
            return connector
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Pinecone: {e}")

    elif db_type.lower() == "qdrant":
        endpoint = kwargs.get("endpoint")
        api_key = kwargs.get("api_key")

        if not endpoint:
            raise ValueError("Qdrant endpoint must be provided")
        try:
            connector = QdrantClient(url=endpoint, api_key=api_key)
            return connector
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Qdrant: {e}")

    else:
        raise ValueError("Unsupported database type. Choose either 'pinecone' or 'qdrant'.")
