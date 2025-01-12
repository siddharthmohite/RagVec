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
