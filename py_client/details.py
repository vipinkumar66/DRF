import requests

endpoint1 = "http://localhost:8000/api/products/1"

response = requests.get(endpoint1)
print(response.json())