def gera_header(json_de_cadastro_ou_login: dict) -> str:
    token  = json_de_cadastro_ou_login.get("token")
    header_path = f"Bearer {token}"
    return {"Authorization": header_path} 