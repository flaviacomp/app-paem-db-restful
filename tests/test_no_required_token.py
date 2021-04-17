from httplib2 import Http
import json

http = Http()
URL_BASE = 'http://localhost:5000'

novaSolicitacaoAcesso = json.dumps({
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
                        })

resp1, result1 = http.request(URL_BASE+'/solicitacoes_acessos/solicitacao_acesso', method='POST', body=novaSolicitacaoAcesso, headers={"Content-Type" : "application/json"})

print("resp 1: ",resp1)
print("result 1:", result1)

novoAcessoPermitido = json.dumps({
                            'id_acesso_permitido':4, 
                            'temperatura':33.6,
                            'hora_entrada':'10:30:38',
                            'hora_saida':'11:20:00',
                            'id_solicitacao_acesso':4
                    })

resp2, result2 = http.request(URL_BASE+'/acessos_permitidos/acesso_permitido', method='POST', body=novoAcessoPermitido, headers={"Content-Type" : "application/json"})

print("resp 2: ",resp2)
print("result 2:", result2)
