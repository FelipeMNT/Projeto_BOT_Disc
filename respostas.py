import random

def receber_resposta(message: str) -> str:
    minuscula = message.lower()

    if minuscula == "olá" or minuscula == "ola":
        return "Fala meu jovem!!"
    if minuscula == "dado":
        return "Qual o tamanho do dado??"
    if minuscula.isnumeric():
        resposta = int(minuscula)
        return str(random.randint(1,resposta))
    if minuscula == "ajuda":
        return "Área sem ajustes por enquanto, favor aguardar."
    return "Eu não entendi o que você quis dizer, tente pedir 'ajuda'!! "