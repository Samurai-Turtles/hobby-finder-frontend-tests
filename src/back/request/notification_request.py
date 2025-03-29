from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    NotificacaoRotas,
)

def get_notificacao(header):
    url = gera_url(ApiConsts.Base, NotificacaoRotas.Get)
    
    requisicao = get(url=url, headers=header)

    return requisicao