import requests

endpoint1 = "http://localhost:8000/api/products/1/update/"
data = {
    "title":"Updated First"
}
response = requests.put(endpoint1, json=data)
print(response.json())