from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    EventoRotas,
    FotoRotas
)

# def colocar_foto(header, id_event: str):
#     url = gera_url(ApiConsts.Base, EventoRotas.Get_By_Id, id_event)
    
#     requisicao = get(url=url, headers=header)

#     return requisicao

# Criar apenas se necessário, pois irá ler fotos e mandar fotos, pode ser meio complicado de fazer