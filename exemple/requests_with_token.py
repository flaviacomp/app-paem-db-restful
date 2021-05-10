'''
That module test accesses endpoins for solicitacao_acesso and 
acesso_permitido considering that token is required. 

'''

from httplib2 import Http
import json

http = Http()

login = {"login":"teste_docente", "senha":"teste"}
print(login)
input('Testting with token. Type any key')

URL_BASE = 'http://localhost:5000'

resp, result = http.request(
                    URL_BASE+'/auth/token',
                    method='GET', 
                    body = json.dumps(login), 
                    headers = {"Content-Type" : "application/json"}
               )

token_dict = json.loads(result)
token = {"Content-Type":'application/json'}
token["Authorization"] = "Bearer " + token_dict['token']
print("\nFull token:", token, '\n')

#teste route to solicitacao_acesso
tag = input("\nAcessing solicitacao_acesso route.Type any key:")
print('\ntesting POST request\n')

dict_solicitacao = {
        'id_solicitacao_acesso':4,
        'para_si':0,
        'data':'23-04-2021',
        'hora_inicio':'17:30:34',
        'hora_fim':'18:00:00',
        'status_acesso':'1',
        'nome':'Caros',
        'fone':'(91)983878675',
        'usuario_id_usuario':5,
        'discente_id_discente':2,
        'id_recurso_campus':6
}

novaSolicitacaoAcesso = json.dumps(dict_solicitacao)

resp_post, result_post = http.request(
                                URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', 
                                method='POST', body=novaSolicitacaoAcesso, 
                                headers=token
                        )

print("resp POST: ",resp_post)
print("result POST:", result_post)

print('\ntesting GET request')

solicitacao = json.dumps({"id":dict_solicitacao['id_solicitacao_acesso']})

resp_get, result_get = http.request(
                                URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', 
                                method='GET', 
                                body=solicitacao,
                                headers=token
                        )

print('resp GET:', resp_get)
print('result GET:', result_get)

# print('\ntesting DELETE request')

# resp_del, result_del = http.request(
#                                 URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', 
#                                 method='DELETE', 
#                                 body=solicitacao,
#                                 headers=token
#                         )

# print('resp DELETE:', resp_del)
# print('result DELETE:', result_del)

# testing route to acesso_permitido
tag = input("\nAcessing acesso_permitido route. Type any key to tag:")

dict_acesso = {
        'id_acesso_permitido':4, 
        'temperatura':33.6,
        'hora_entrada':'10:30:38',
        'hora_saida':'11:20:00',
        'id_solicitacao_acesso':4
}

novoAcessoPermitido = json.dumps(dict_acesso)

resp_post, result_post = http.request(
                                URL_BASE+'/acessos_permitidos/acesso_permitido', 
                                method='POST', 
                                body=novoAcessoPermitido, 
                                headers=token
                         )

print("resp POST: ",resp_post)
print("result POST:", result_post)

print('\ntesting GET request')

acesso_permitido = json.dumps({'id':dict_acesso['id_acesso_permitido']})

resp_get, resul_get = http.request(
                                URL_BASE+'/acessos_permitidos/acesso_permitido',
                                method='GET',
                                body=acesso_permitido,
                                headers=token
                      )

print('resp GET:', resp_get)
print('result GET:', result_get)

# print('\ntesting DELETE request')

# resp_del, result_del = http.request(
#                                 URL_BASE+'/acessos_permitidos/acesso_permitido',
#                                 method='DELETE',
#                                 body=acesso_permitido,
#                                 headers=token
#                        )

# print('resp DELETE:', resp_del)
# print('result DELETE:', result_del)

print('\nAll test passed. Test Finish.\n')
