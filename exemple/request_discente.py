# request a discente in data base by matricula param.
import requests

# change TOKEN to valide token
headers = {"Authorization":f"Bearer TOKEN"}
payload = {"matricula":"2019013473"}

res = requests.get("http://localhost:5000/discentes/discente", params=payload, headers=headers)

print("status_code: ",res.status_code)
print("headers: ", res.headers)
print("encoding: ", res.encoding)
print("text: ", res.text)
print("json: ", res.json())