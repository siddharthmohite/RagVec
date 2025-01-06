from base.abstract import VectorDatabase
from connect import connect

class PineCone(VectorDatabase):
    def __init__(self, **kwargs):
        self.connector = connect("pinecone")

    def create_collection(self, name, dimension, **kwargs) -> None:
        """
        Creating a new Pinecone index with optional settings
        """

        pod_type = kwargs.get("pod_type", "p1")
        replicas = kwargs.get("replicas", 1)
        metadata_config = kwargs.get("metadata_config", None)

        try:
            self.connector.create_index(
                name = name,
                dimension = dimension,
                pod_type = pod_type,
                replicas = replicas,
                metadata_config = metadata_config
            )
            print(f"created collection {name} with dimension {dimension}")
        except Exception as e:
            print(f"Failed while creating collection {name}: {e}")