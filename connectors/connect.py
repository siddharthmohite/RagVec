# connectors/connect.py
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from pinecone import Pinecone

load_dotenv()  # Load environment variables

def connection(db_type: str):
    """
    Creates a connection to either Pinecone or Qdrant, based on the db_type.
    :param db_type: "pinecone" or "qdrant"
    :return: Connection object
    """
    if db_type.lower() == "pinecone":
        pinecone_api_key = os.getenv("PINECONE_API_KEY_REMOTE")
        environment = os.getenv("PINECONE_ENVIRONMENT")

        if not pinecone_api_key or not environment:
            raise ValueError(
                "Pinecone API Key and environment must be provided via environment variables."
            )
        try:
            connector = Pinecone(api_key=pinecone_api_key, environment=environment)
            return connector
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Pinecone: {e}")

    elif db_type.lower() == "qdrant":
        local_endpoint = os.getenv("QDRANT_ENDPOINT_LOCAL")
        local_api_key = os.getenv("QDRANT_API_KEY_LOCAL")
        remote_endpoint = os.getenv("QDRANT_ENDPOINT_REMOTE")
        remote_api_key = os.getenv("QDRANT_API_KEY_REMOTE")

        if local_endpoint:
            endpoint = local_endpoint
            api_key = local_api_key
        elif remote_endpoint:
            endpoint = remote_endpoint
            api_key = remote_api_key
        else:
            raise ValueError(
                "No Qdrant endpoint configured. Set QDRANT_ENDPOINT_LOCAL or QDRANT_ENDPOINT_REMOTE in the .env file."
            )

        try:
            connector = QdrantClient(url=endpoint, api_key=api_key)
            return connector
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Qdrant: {e}")

    else:
        raise ValueError("Unsupported database type. Choose either 'pinecone' or 'qdrant'.")
