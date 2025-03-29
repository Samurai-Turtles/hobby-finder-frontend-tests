from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    UsuarioRotas,
    ParticipacaoRotas
)

def atualiza_participacao_presenca(header, id_event: str, id_participacao: str, presenca: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, ParticipacaoRotas.Get_By_Evento, id_participacao)
    
    requisicao = put(url=url, headers=header, params={
        "userParticipation": presenca
    })

    return requisicao

def atualiza_participacao(header, id_event: str, id_participacao: str, participacao):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, ParticipacaoRotas.Get_By_Evento, id_participacao)
    
    requisicao = put(url=url, headers=header, json=participacao)

    return requisicao

def deleta_participacao(header, id_event: str, id_participacao: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, ParticipacaoRotas.Get_By_Evento, id_participacao)
    
    requisicao = delete(url=url, headers=header)

    return requisicao

def get_participacao_by_auth(header, size: int, page: int):
    url = gera_url(ApiConsts.Base, UsuarioRotas.Base, ParticipacaoRotas.Base)
    
    requisicao = get(url=url, headers=header, params={
        "size": size,
        "page": page
    })

    return requisicao

def get_participacao_by_evento(header, id_evento: str, size: int, page: int):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_evento, ParticipacaoRotas.Base)
    
    requisicao = get(url=url, headers=header, params={
        "size": size,
        "page": page
    })

    return requisicao

def deleta_participacao(header, id_event: str, id_participacao: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, ParticipacaoRotas.Get_By_Evento, id_participacao)
    
    requisicao = delete(url=url, headers=header)

    return requisicao