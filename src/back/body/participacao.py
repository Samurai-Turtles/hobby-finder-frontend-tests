# enum presença
def presenca_confirmada():  return "CONFIRMED_PRESENCE"
def presence_unconfirmed(): return "UNCONFIRMED_PRESENCE"

# enum participação
def participante(): return "PARTICIPANT"
def admin(): return "ADMIN"
def creator(): return "CREATOR"

def participacao_update(participacao: str, posicao: str):
    return {
        "participation": participacao,
        "position": posicao
    }