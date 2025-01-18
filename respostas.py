import api


def receber_resposta(texto: str) -> str:
    global nome, plataformas_info, generos_info
    minuscula = texto.lower()

    if minuscula == "olá" or minuscula == "ola":
        return """Fala meu jovem!!
        \n==================================\n
        Menu de interação
        \n==================================\n
        1- Receber indicação de jogo aleatório\n
        2- Receber indicação por gênero de jogo\n
        3- Deseja ver a definição do que é JOGO?\n
        4- Ajuda\n
        \n==================================\n"""
    match minuscula:
        case "1":
            nome, plataformas_info, generos_info = api.igdb()
            return f"""Você selecionou a opção 1.
                    \nNome do Jogo: {nome}
                    \nGênero: {', '.join(generos_info)}
                    \nPlataforma: {', '.join(plataformas_info)}"""
        case "2":
            return f""

        case "3":
            return "https://www.youtube.com/watch?v=j-wH8EPJ03U&t=1s&ab_channel=Zangado"

        case "4":
            return "Comandos de ativação: Olá, 1, 2, categoria: coloque a categoria desejada, ajuda\n\nCaso queira receber as mensagens no seu privado, coloque uma '!' no inicio de cada comando."

        case _:
            return "Eu não entendi o que você quis dizer, tente pedir 'ajuda'!!\n"
