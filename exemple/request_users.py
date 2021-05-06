import requests

payload = {"login":"teste_docente", "senha":"teste"}
res = requests.get("http://localhost:5000/login", params=payload)
token = res.json().get("token")
print("Token", token)

headers = {"Authorization":f"Bearer {token}", "Content-Type": "application/json"}

res = requests.get("http://localhost:5000/users", headers=headers)

print("status_code: ",res.status_code)
print("headers: ", res.headers)
print("encoding: ", res.encoding)
print("text: ", res.text)
print("json: ", res.json())