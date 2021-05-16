from .base_test import BaseTest
from ..resources import UsuarioResource
#teste route to usuario


def run_test_usuario():
    
    tag = input("\nTesting USUARIO route type enter to continue:")


    URL = BaseTest.get_url(UsuarioResource.ROUTE)

    # add query strings
    payload = {}

    body_post = { 
            "matricula": "11111111111",
            "nome": "Test Discente 1",
            "curso_id_curso":2,
            "cpf":"22222222222",
            "entrada":"2021",
            "semestre":1,
            "endereco":"endereço teste",
            "grupo_risco":0,
            "status_covid":0,
            "status_permissao":1,
            "usuario_id_usuario":5
        }

    body_put ={ 
        "matricula": "11111111111",
        "nome": "Test Discente 2",
        "curso_id_curso":3,
        "cpf":"22222222222",
        "entrada":"2021",
        "semestre":1,
        "endereco":"endereço teste Updated",
        "grupo_risco":0,
        "status_covid":0,
        "status_permissao":1,
        "usuario_id_usuario":5
    }


    payload['id_usuario'] = BaseTest.post(URL, body_post)

    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, payload)