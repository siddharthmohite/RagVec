import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from connectors.pinecone_adapter import PineConeDB
from factory.factory import VectorDBFactory
from qdrant_client.http.models import Distance
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


def get_qdrant_settings():
    qdrant_api_key = os.getenv("QDRANT_API_KEY_REMOTE")
    qdrant_endpoint = os.getenv("QDRANT_ENDPOINT_REMOTE")
    # Initialize the factory for Qdrant
    db = VectorDBFactory(
        db_type="qdrant",
        api_key=qdrant_api_key,
        endpoint=qdrant_endpoint,
    )
    return db

def get_pinecone_settings():
    pinecone_api_key = os.getenv("PINECONE_API_KEY_REMOTE")
    # Initialize the factory for Pinecone
    db = VectorDBFactory(
        db_type="pinecone",
        api_key=pinecone_api_key,
    )
    return db

db_qdrant  = get_qdrant_settings()
db_pinecone = get_pinecone_settings()

def test_create_collection():
    """
    Testing create collection method qdrant and pinecone
    """
    db_qdrant.create_collection(
                name = "Siddharth's testing",
                dimension = 128,
                distance = Distance.COSINE,
    )

    db_pinecone.create_collection(
         name="testing",
            dimension=128,
            metric="cosine",
            cloud="aws",
            region="us-east-1"
    )

def test_get_collection_details():
    """
     Testing Get collection details
    """
    name_qdrant ="testing"
    name_pinecone = "testing"
    db_qdrant.get_collection_details(name_qdrant)
    db_pinecone.get_collection_details(name_pinecone)

def test_list_all_collections():
    db_qdrant.list_all_collections()
    db_pinecone.list_all_collections()
           
def test_delete_collection():
    """
    Testing delete a collection
    """
    name_qdrant = "testing"
    name_pinecone = "testing"
    db_qdrant.delete_collection(name_qdrant)
    db_pinecone.delete_collection(name_pinecone)

if __name__ == "__main__":
    # Create Collection
    test_create_collection()
    # Get Collection details
    test_get_collection_details()
    # List All collections
    test_list_all_collections()
    # Delete a collection
    test_delete_collection()
