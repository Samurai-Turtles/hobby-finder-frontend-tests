def local(street: str, district: str, number: str, city: str, state: str, longitude: float, latitude: float):
    return {
        "street": street,
        "district": district,
        "number": number,
        "city": city,
        "state": state,
        "longitude": longitude,
        "latitude": latitude
    }

# enum privacidade
def privado(): return "PRIVATE"
def publico(): return "PUBLIC"

def evento(name: str, begin: str, end: str, local: dict, privacidade: str, descricao: str, maximum: int):
    return {
        "name": name,
        "begin": begin,
        "end": end,
        "local": local,
        "privacidade": privacidade,
        "descricao": descricao,
        "max": maximum
    }