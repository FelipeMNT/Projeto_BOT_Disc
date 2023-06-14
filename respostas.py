import random
import pandas as pd

caminhoDataBase = 'DataBase jogos.csv'
df = pd.read_csv(caminhoDataBase)
df.index = [int(x) for x in range(1, df.index.size + 1)]

def receber_resposta(texto: str) -> str:
    minuscula = texto.lower()

    if minuscula == "olá" or minuscula == "ola":
        return """Fala meu jovem!!
        \n==================================\n
        Menu de interação
        \n==================================\n
        1- Receber indicação de jogo aleatório\n
        2- Receber indicação por categoria de jogo\n
        3- Ajuda\n
        \n==================================\n"""
    match minuscula:
        case "1":

            jogo_aleatorio = df.sample()

            nome = jogo_aleatorio['nome'].values[0]
            data = jogo_aleatorio['data lançamento'].values[0]
            categoria = jogo_aleatorio['categoria'].values[0]
            dev = jogo_aleatorio['desenvolvedor'].values[0]

            indicacao = f"Jogo aleatório: {nome}\nData de lançamento: {data}\nCategoria: {categoria}\nDesenvolvedor: {dev}"

            return f"Aqui está uma indicação de jogo aleatório:\n\n{indicacao}"
        
        case "2":
            return "Informe a categoria de jogo desejada.\n(Informe a categoria da seguinte forma: 'categoria: nome da categoria desejada'.)"

        case _ if minuscula.startswith("categoria:"):
            categoria_desejada = minuscula.split(":")[1].strip()

            jogos_na_categoria = df[df['categoria'].str.lower() == categoria_desejada]
            if jogos_na_categoria.empty:
                return f"Não há jogos disponíveis na categoria {categoria_desejada}."

            jogo_aleatorio = jogos_na_categoria.sample()

            nome = jogo_aleatorio['nome'].values[0]
            data = jogo_aleatorio['data lançamento'].values[0]
            categoria = jogo_aleatorio['categoria'].values[0]
            dev = jogo_aleatorio['desenvolvedor'].values[0]

            indicacao = f"Jogo aleatório: {nome}\nData de lançamento: {data}\nCategoria: {categoria}\nDesenvolvedor: {dev}"

            return f'Aqui está uma indicação de jogo aleatório na categoria "{categoria_desejada}":\n\n{indicacao}'


        case "ajuda":
            return "Comandos de ativação: Olá, 1, 2, categoria: coloque a categoria desejada, ajuda\n\nCaso queira receber as mensagens no seu privado, coloque uma '!' no inicio de cada comando."

        case _:
            return "Eu não entendi o que você quis dizer, tente pedir 'ajuda'!!\n"
