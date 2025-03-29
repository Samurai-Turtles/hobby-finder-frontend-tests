from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    AvaliacaoRotas
)

def get_evaluation(header, id_event: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, AvaliacaoRotas.Get)
    
    requisicao = get(url=url, headers=header)

    return requisicao

def post_evaluation(header, id_event: str, avaliacao):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, AvaliacaoRotas.Post)
    
    requisicao = post(url=url, json=avaliacao, headers=header)

    return requisicao
