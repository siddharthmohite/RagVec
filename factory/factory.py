# factory.py
from connectors.pinecone_adapter import PineConeDB
from connectors.qdrant_adapter import QdrantDB

class VectorDBFactory:
    def __init__(self, db_type: str, **kwargs):
        self.db = self._get_client(db_type, **kwargs)

    def _get_client(self, db_type: str, **kwargs):
        if db_type.lower() == "pinecone":
            return PineConeDB(**kwargs)
        elif db_type.lower() == "qdrant":
            return QdrantDB(**kwargs)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

    # Unified interface for collections
    def create_collection(self, name: str, dimension: int, **kwargs):
        return self.db.create_collection(name, dimension, **kwargs)
    
    def get_collection_details(self, name:str):
        return self.db.get_collection_details(name)
    
    def list_all_collections(self):
        return self.db.list_all_collections()

    # def delete_collection(self, name: str):
    #     return self.db.delete_collection(name)

    # # Unified interface for vectors
    # def upsert_vectors(self, collection: str, vectors: list):
    #     return self.db.upsert_vectors(collection, vectors)

    # def search_vectors(self, collection: str, query_vector: list, top_k: int, **kwargs):
    #     return self.db.search_vectors(collection, query_vector, top_k, **kwargs)
