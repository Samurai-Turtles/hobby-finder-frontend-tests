def gera_url(*args: str) -> str:
    return "/".join(parte_url for parte_url in args if parte_url != "/")