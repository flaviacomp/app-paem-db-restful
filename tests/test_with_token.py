from httplib2 import Http
import json

h = Http()

data = {"login":"teste_docente", "senha":"teste"}

url_token = 'http://localhost:5000/auth/token'

resp, result = h.request(url_token,'GET', body = json.dumps(data), headers = {"Content-Type" : "application/json"})
token_dict = json.loads(result)[0]
token = "Bearer " + token_dict['token']


print("Full token:", token)

url_users = 'http://localhost:5000/solicitacoes_acessos'

resp, result = h.request(url_users, method='GET', headers = {"Authorization" : token})
print()
users_dict = json.loads(result)

print(users_dict)
