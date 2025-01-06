from abc import ABC, abstractmethod


class VectorDatabase(ABC):
    """
    Abstract base class that defines the interface for vector database adapters.
    All concrete adapters (e.g., PineconeDB, QdrantDB) must implement these methods.
    """

    @abstractmethod
    def create_collection(self, name: str, dimension: int, **kwargs) -> None:
        """
        Create a new collection (or index) in the vector database.

        :param name: Name of the collection/index to create.
        :param dimension: Dimensionality of the vectors in the collection.
        :param kwargs: Additional parameters specific to the database.
        """
        pass
