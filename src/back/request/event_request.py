from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    UsuarioRotas
)

def get_evento(header, id_event: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event)
    
    requisicao = get(url=url, headers=header)

    return requisicao

def atualiza_evento(header, id_evento: str, evento_update_dto):
    url = gera_url(ApiConsts.Base, EventoRotas.Put, id_evento)

    requisicao = put(url=url, json=evento_update_dto, headers=header)

    return requisicao


def delete_evento(header, id_event: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Delete, id_event)
    
    requisicao = delete(url=url, headers=header)

    return requisicao


def get_eventos(header, latitude: float = None, longitude: float = None, qtd_eventos: float = None, pagina: int = 0, nome: str = str()):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Auth)
    
    requisicao = get(url=url, headers=header, params = {
        "longitude": longitude,
        "latitude": latitude,
        "eventsPerPage": qtd_eventos,
        "page": pagina,
        "name": nome,
    })

    return requisicao

def post_evento(header, user_register):
    url = gera_url(ApiConsts.Base, EventoRotas.Post)
    
    requisicao = get(url=url, headers=header, json = user_register)

    return requisicao

def get_evento_por_usuario(header, usuario_id: str, qtd_eventos: float = None, pagina: int = 0, nome: str = str()):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, UsuarioRotas.Get, usuario_id)
    
    requisicao = get(url=url, headers=header, params={
        "eventsPerPage": qtd_eventos,
        "page": pagina,
        "name": nome,
    })

    return requisicao