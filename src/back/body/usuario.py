def usuario_registrar(email: str, username: str, password: str, nomeCompleto: str):
    return {
        "email": email,
        "username": username,
        "password": password,
        "nomeCompleto": nomeCompleto
    }

# Enum de interesse
def esporte(): return "SPORT"
def anime():   return "ANIME"

def usuario_put(email: str, username: str, password: str, nomeCompleto: str, bio: str, interesses: list[str]):
    return {
        "email": email,
        "username": username,
        "password": password,
        "nomeCompleto": nomeCompleto,
        "bio": bio,
        "interesses": interesses
    }

def login(login: str, password: str):
    return {
        "login": login,
        "password": password
    }