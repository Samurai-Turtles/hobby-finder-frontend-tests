import json
import pathlib
import logging

def carregar_configuracao():
    configuracao = {
       "url": "http://localhost:8080/api"
    }
    try:
        with open("config.json") as config_file:
            configuracao = json.load(config_file)
    except Exception:
        pass

    return configuracao