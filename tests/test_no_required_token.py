
'''
That modele test acesses endpoins for solicitacao_acesso and 
acesso_permitido considering any token is'nt required. 

'''

from httplib2 import Http
import json

http = Http()
URL_BASE = 'http://localhost:5000'

#teste route to solicitacao_acesso
tag = input("Acessing solicitacao_acesso route.Type any key:")
print('testing POST request')

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
                                headers={"Content-Type" : "application/json"}
                        )

print("resp POST: ",resp_post)
print("result POST:", result_post)

print('testing GET request')

solicitacao = json.dumps({"id":dict_solicitacao['id_solicitacao_acesso']})

resp_get, result_get = http.request(
                                URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', 
                                method='GET', 
                                body=solicitacao,
                                headers={'Content-Type':"application/json"}
                        )

print('resp GET:', resp_get)
print('result GET:', result_get)

print('testing DELETE request')

resp_del, result_del = http.request(
                                URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', 
                                method='DELETE', 
                                body=solicitacao,
                                headers={'Content-Type':"application/json"}
                        )

print('resp DELETE:', resp_del)
print('result DELETE:', result_del)

# testing route to acesso_permitido
tag = input("Acessing acesso_permitido route. Type any key to tag:")

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
                                headers={"Content-Type" : "application/json"}
                         )

print("resp POST: ",resp_post)
print("result POST:", result_post)

print('testing GET request')

acesso_permitido = json.dumps({'id':dict_acesso['id_acesso_permitido']})

resp_get, resul_get = http.request(
                                URL_BASE+'/acessos_permitidos/acesso_permitido',
                                method='GET',
                                body=acesso_permitido,
                                headers={'Content-Type':'application/json'}
                      )

print('resp GET:', resp_get)
print('result GET:', result_get)

print('testing DELETE request')

resp_del, result_del = http.request(
                                URL_BASE+'/acessos_permitidos/acesso_permitido',
                                method='DELETE',
                                body=acesso_permitido,
                                headers={'Content-Type':'application/json'}
                       )

print('resp DELETE:', resp_del)
print('result DELETE:', result_del)

print('\nAll test passed. Test Finish.\n')