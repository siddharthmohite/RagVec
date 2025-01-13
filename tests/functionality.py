import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from connectors.pinecone_adapter import PineConeDB
from factory.factory import VectorDBFactory
from qdrant_client.http.models import Distance
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def test_qdrant_collection():
    """
    Test creating a real Qdrant collection using the library.
    """
    # Load Qdrant credentials from environment variables
    qdrant_api_key = os.getenv("QDRANT_API_KEY_REMOTE")
    qdrant_endpoint = os.getenv("QDRANT_ENDPOINT_REMOTE")
    # Initialize the factory for Qdrant
    db = VectorDBFactory(
        db_type="qdrant",
        api_key=qdrant_api_key,
        endpoint=qdrant_endpoint,
    )
    name = "test_qdrant_collection"
    # Create a collection
    try:
        db.get_collection_details(name)
        # db.create_collection(
        #     name="test_qdrant_collection",
        #     dimension=128,
        #     distance=Distance.COSINE,  # Qdrant-specific distance metric
        # )
        # print("Qdrant: Successfully created the collection 'test_qdrant_collection'.")
    except Exception as e:
        print(f"Qdrant: Failed to get the collection details {name}: {e}")


def test_pinecone_collection():
    """
    Test creating a real Pinecone collection using the library.
    """
    # Load Pinecone credentials from environment variables
    pinecone_api_key = os.getenv("PINECONE_API_KEY_REMOTE")
    print(pinecone_api_key)

    # Initialize the factory for Pinecone
    db = VectorDBFactory(
        db_type="pinecone",
        api_key=pinecone_api_key,
    )

    # Create an index (collection) in Pinecone
    # try:
    #     db = PineConeDB()

    #     db.create_collection(
    #         name="testing",
    #         dimension=128,
    #         metric="cosine",
    #         cloud="aws",
    #         region="us-east-1"
    #     )
    # except Exception as e:
    #     print(f"Pinecone: Failed to create the collection: {e}")
    #     return
    name = "testing"
    try:
        db.get_collection_details(name)
    except Exception as e:
        print(f"Pinecone: Failed to create the collection: {e}")
        return
    

if __name__ == "__main__":
    # print("Testing Qdrant functionality...")
    # test_qdrant_collection()

    print("\nTesting Pinecone functionality...")
    test_pinecone_collection()
