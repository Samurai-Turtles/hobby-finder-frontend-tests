from httpx import head
from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    UsuarioRotas,
    SolicitacaoRotas
)

def atualiza_solicitacao(header, id_event: str, id_request: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, SolicitacaoRotas.Get_By_Evento, id_request)
    
    requisicao = put(url=url, headers=header)

    return requisicao

def deleta_solicitacao(header, id_event: str, id_request: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, SolicitacaoRotas.Get_By_Evento, id_request)
    
    requisicao = delete(url=url, headers=header)

    return requisicao

def obtem_solicitacoes_por_evento(header, id_evento: str, size: int, page: int):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_evento, SolicitacaoRotas.Get_By_Evento)

    requisicao = get(url=url, headers=header, params={
        "size": size,
        "page": page
    })
    
    return requisicao

def cria_solicitacao(header, id_evento: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_evento, SolicitacaoRotas.Post)

    requisicao = post(url=url, headers=header)

    return requisicao

def obtem_solicitacoes_por_auth(header, size: int, page: int):
    url = gera_url(ApiConsts.Base, UsuarioRotas.Get,  SolicitacaoRotas.Get_By_Evento)

    requisicao = get(url=url, headers=header, params={
        "size": size,
        "page": page
    })

    return requisicao

def deleta_solicitacao_por_usuario(header, id_solicitacao):
    url = gera_url(ApiConsts.Base, UsuarioRotas.Get,  SolicitacaoRotas.Get_By_Evento, id_solicitacao)

    requisicao = delete(url=url, headers=header)

    return requisicao