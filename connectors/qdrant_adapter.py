from base.abstract import VectorDatabase
from connectors.connect import connection
from qdrant_client import models

class QdrantDB(VectorDatabase):
    def __init__(self, **kwargs):
        """
        Initialize QdrantDB by creating a connection using provided parameters.
        :param kwargs: Contains `api_key`, `endpoint`, and other optional parameters.
        """
        self.connector = connection("qdrant", **kwargs)

    def create_collection(self, name: str, dimension: int, **kwargs) -> None:
         """
         Creates a new qdrant collection with extra setting options
         """
          # Remove distance from kwargs if it exists
         kwargs.pop("distance", None)
         vectors_config = models.VectorParams(size=dimension, distance=models.Distance.COSINE)
         try:
             self.connector.create_collection(
                 collection_name = name,
                 vectors_config = vectors_config,
                 **kwargs
             )
             print(f" QDrant: Created collection {name} with dimension {dimension}")
         except Exception as e:
             raise RuntimeError(f"QDrant: Failed to create collection {name}: {e}")

    def get_collection_details(self, name:str) -> None:
        """
        Get all the collection details provided with a name
        """
        try:
            result = self.connector.get_collection(name)
            print(result)
        except Exception as e:
            raise RuntimeError(f"QDrant: Failed to get collection details {name} : {e}")    

    def list_all_collections(self) -> None:
        """
        List all collections
        """
        try:
            all_collections = self.connector.get_collections()
            print(all_collections) 
        except Exception as e:
            raise RuntimeError(f"Qdrant failed to List collections : {e}")

    def delete_collection(self, name: str) -> None:
        """
        Delete's a collection with a given name
        """
        try:
            response = self.connector.delete_collection(name)
            print(response)
        except Exception as e:
            raise RuntimeError(f"Qdrant: Failed to delete collection with {name} : {e}")