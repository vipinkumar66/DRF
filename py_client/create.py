import requests

endpoint1 = "http://localhost:8000/api/products/"

data = {
    "title":"This is through mixins",
    "price":100.00
}
response = requests.post(endpoint1, json=data)
print(response.json())