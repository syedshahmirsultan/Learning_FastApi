import requests
from requests.models import Response

response : Response = requests.get("http://127.0.0.1:8000/hi/Shahmir")

print(response.status_code)
print(response.headers)
print(response.json())
print(response.text)