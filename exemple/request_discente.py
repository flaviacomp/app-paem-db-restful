import requests
import json

# change TOKEN to valide token
headers = {"Authorization":f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwIjoxNjIwMjYxMDUyfQ.H33J6liTg6aMFcejVDcmmqRhgRUX7MnG1EK6OfsI0ZA"}
payload = {"matricula":"2019013473"}

res = requests.get("http://localhost:5000/discentes/discente", params=payload, headers=headers)

print("status_code: ",res.status_code)
print("headers: ", res.headers)
print("encoding: ", res.encoding)
print("text: ", res.text)
print("json: ", res.json())