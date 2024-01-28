from fastapi.testclient import TestClient
import requests

# Access the FastAPI app running in another container
fastapi_url = "http://fastapi-app:80"
client = TestClient(None)

# Example 1: Test the root endpoint
response = requests.get(fastapi_url + "/")
print(response.json())

# Example 2: Test the /items/{item_id} endpoint
response = requests.get(fastapi_url + "/items/42?q=test")
print(response.json())
