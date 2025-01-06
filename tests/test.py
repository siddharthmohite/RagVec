# tests/test_pinecone.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connectors.connect import connect  # Import the connect function
from dotenv import load_dotenv

load_dotenv()

def test_pinecone_connection():
  try:
       connector = connect(db_type = "pinecone")  # By default, it will use the wrapper.
       # I can also pass use_wrapper = False here for testing
       print(connector.config)
       


  except Exception as e:
     print("Pinecone connection or health check failed:", e)

def test_qdrant_connection():
  try:
       connection_result = connect(db_type = "Qdrant")
       print(connection_result)

  except Exception as e:
     print("Qdrant connection or health check failed:", e)



if __name__ == "__main__":
    test_pinecone_connection()
    test_qdrant_connection()