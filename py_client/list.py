import requests

endpoint1 = "http://localhost:8000/api/products/"
endpoint2 = "http://localhost:8000/api/auth/"

authdata = {
    "username":"vipin",
    "password":"vipin123"
}
auth_response = requests.post(endpoint2, json=authdata)
if auth_response.status_code == 200:
    authtoken = auth_response.json()["token"]
    headers = {
        "Authorization" : f"Bearer {authtoken}"
    }
    response = requests.get(endpoint1, headers=headers)
    print(response.json())