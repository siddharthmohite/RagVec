from base.abstract import VectorDatabase
from connect import connect

class QdrantDB(VectorDatabase):
    def __init__(self, **kwargs):
        self.connector = connect("qdrant")

    def create_collection(self, name: str, dimension: int, **kwargs) -> None:
         """
         Creates a new qdrant collection with extra setting options
         """

         distance = kwargs.get("distance", "cosine")
         shard_number = kwargs.get("shard_number", 1)
         on_disk_payload = kwargs.get("on_disk_payload", False)
         try:
             self.connector.create_collection(
                 collection_name = name,
                 vector_size = dimension,
                 distance = distance,
                 shard_number = shard_number,
                 on_disk_payload =  on_disk_payload
             )
             print(f" QDrant: Created collection {name} with dimension {dimension}")
         except Exception as e:
             raise RuntimeError(f"QDrant: Failed to create collection {name}: {e}")
