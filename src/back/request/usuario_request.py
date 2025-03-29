from requests import delete, get, post, put
from src.back.request.gerador_url import gera_url

from src.back.routes import (
    ApiConsts,
    UsuarioRotas
)

def update_auth_user(header, user_update_dto):
    url = gera_url(ApiConsts.Base, UsuarioRotas.login)
    
    requisicao = put(url=url, json=user_update_dto, headers=header)

    return requisicao

def register_user(user_register_dto):
    url = gera_url(ApiConsts.Base, UsuarioRotas.Post)
    
    requisicao = post(url=url, json=user_register_dto)

    return requisicao

def logout_user(header):
    url = gera_url(ApiConsts.Base, UsuarioRotas.logout)
    
    requisicao = post(url=url, headers=header)

    return requisicao

def login_user(header, user_login_dto):
    url = gera_url(ApiConsts.Base, UsuarioRotas.login)
    
    requisicao = post(url=url, json = user_login_dto, headers=header)

    return requisicao

def get_login_user(header, id: str):
    url = gera_url(ApiConsts.Base, UsuarioRotas.Get, id)

    requisicao = get(url=url, headers=header)

    return requisicao

def recover_password(header):
    url = gera_url(ApiConsts.Base, UsuarioRotas.recovery_password)

    requisicao = delete(url=url, headers=header)

    return requisicao

def recover_password(header):
    url = gera_url(ApiConsts.Base, UsuarioRotas.dele)

    requisicao = delete(url=url, headers=header)

    return requisicao
