import requests


# change TOKEN to valide token
headers = {"Authorization":f"Bearer TOKEN", "Content-Type": "application/json"}

res = requests.get("http://localhost:5000/discentes", headers=headers)

print("status_code: ",res.status_code)
print("headers: ", res.headers)
print("encoding: ", res.encoding)
print("text: ", res.text)
print("json: ", res.json())