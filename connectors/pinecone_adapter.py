from base.abstract import VectorDatabase
from connectors.connect import connection
from pinecone import ServerlessSpec

class PineConeDB(VectorDatabase):
    def __init__(self, **kwargs):
        self.connector = connection("pinecone")

    def create_collection(self, name, dimension, **kwargs) -> None:
        """
        Create a new Pinecone index with optional settings.
        """
        # Optional parameters for Pinecone's create_index
        cloud = kwargs.get("cloud", "aws")
        region = kwargs.get("region", "us-east-1")
        metric = kwargs.get("metric", "cosine")  # Metric: cosine, dotproduct, or euclidean

        try:
            self.connector.create_index(
                name=name,
                dimension=dimension,
                metric=metric,
                spec=ServerlessSpec(
                    cloud=cloud,
                    region=region
                )
            )
        except Exception as e:
            print(f"Pinecone: Failed to create index '{name}': {e}")
            return  # Exit the function if an exception occurs

        # Only print this message if the creation succeeds
        print(f"Pinecone: Successfully created index '{name}' with dimension {dimension} and metric {metric}.")

    def get_collection_details(self, name: str) -> None:
        """
        Gets index description from pinecone for a given index
        """

        try:
            index_description = self.connector.describe_index(name)
            print(index_description)
        except Exception as e:
            raise ValueError(f"Pinecone: Failed to retrieve index details with {name} : {e}")    


    def list_all_collections(self) -> None:
        """
        List all indexes inside Pinecone 
        """
        try:
            all_collections = self.connector.list_indexes()
            print(all_collections)
        except Exception as e:
            raise RuntimeError(f"Pinecone: Failed to list all collections : {e}")    