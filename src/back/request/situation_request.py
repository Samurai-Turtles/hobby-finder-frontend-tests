from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    SituacaoRotas
)

def get_evento(header, id_event: str):
    url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event, SituacaoRotas.Base)
    
    requisicao = get(url=url, headers=header)

    return requisicao