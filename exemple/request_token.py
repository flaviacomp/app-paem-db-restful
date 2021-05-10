# make login request and get a token to access ather routes with it.
import requests

payload = {"login":"teste_docente", "senha":"teste"}
res = requests.get("http://localhost:5000/login", params=payload)

print(res.json().get("token"))
