import os
import unittest
from unittest.mock import patch, MagicMock
from factory.factory import VectorDBFactory
from qdrant_client import models

from dotenv import load_dotenv
load_dotenv()

class TestCreateCollection(unittest.TestCase):
    def setUp(self):
        """
        Setup environment variables for pinecone and qdrant for testing
        """
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY_REMOTE", "mock_pinecone_key")
        self.pinecone_env = os.getenv("PINECONE_ENVIRONMENT", "mock_env")
        self.qdrant_api_key = "mock_qdrant_key"
        self.qdrant_endpoint = "http://mock-qdrant"


    # @patch("connectors.connect.connection")
    # def test_create_pinecone_collection(self,mock_pinecone):
    #     """
    #     Test Creating a collection in Pinecone with extra settings
    #     """

    #     mock_client = MagicMock()
    #     mock_pinecone.init.return_value = None
    #     mock_pinecone.create_index = mock_client.create_index

    #     db = VectorDBFactory(
    #         db_type = "pinecone",
    #         api_key = self.pinecone_api_key,

    #     )

    #     db.create_collection(name = "unittest", dimension = 128)

    #     mock_client.create_index.assert_called_once_with(
    #         name="test_pinecone_collection",
    #         dimension=128
    #     )
    
    @patch("connectors.connect.QdrantClient")
    @patch("connectors.connect.connection")
    @patch("builtins.print")
    def test_create_qdrant_collection(self,mock_print, mock_connection ,mock_qdrant_client):
        """
        Test Creating a Qdrant Collection with optional settings
        """

        mock_client_instance = MagicMock()
        mock_qdrant_client.return_value = mock_client_instance
        mock_connection.return_value = mock_client_instance
        
        db = VectorDBFactory(
            db_type = "qdrant",
            api_key = self.qdrant_api_key,
            endpoint = self.qdrant_endpoint,
        )

        db.create_collection(
            name = "unittest",
            dimension=128,
            distance=models.Distance.COSINE,  # Qdrant-specific setting
        )

        mock_print.assert_called_once_with(" QDrant: Created collection unittest with dimension 128")

        mock_client_instance.create_collection.assert_called_once_with(
            collection_name = "unittest",
            vectors_config=models.VectorParams(size=128, distance=models.Distance.COSINE),
        )
if __name__ == "__main__":
    unittest.main()            