import requests

pk_id = input("Enter the id of the object which you want to delete")
try:
    pk_id = int(pk_id)
except:
    pk_id = None

if pk_id:
    endpoint = f"http://localhost:8000/api/products/{pk_id}/delete/"
    response = requests.delete(endpoint)
    print(response.status_code)