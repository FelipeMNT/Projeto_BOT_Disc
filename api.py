import requests
import random

nome = []
plataformas_info = []
generos_info = []


def igdb():
    global nome, plataformas_info, generos_info
    # Aqui é o nosso "login" da api
    client_id = "ID FORNECIDO PELA TWITCH"
    access_token = "TOKEN FORNECIDO POR MÉTODO POST PELO IGDB"

    # Aqui é a definição de cada url que a gente vai precisar, tem mais umas, poreeeem, não vamos precisar ainda
    url_jogos = "https://api.igdb.com/v4/games/"
    url_plataformas = "https://api.igdb.com/v4/platforms/"
    url_generos = "https://api.igdb.com/v4/genres/"
    url_videos = "https://api.igdb.com/v4/game_videos"

    # Aqui é a construção padrão pra acessar a api, definitivamente, sempre vai ser isso
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }

    # Essa variável vai facilitar nossa vida na hora de aplicar no bot
    # A variação 1000 e 9999 pode ser literalmente qualquer numero que agente decidir, o ideal é...
    # Colocar um número beeem alto justamente pra abranger todos os jogos do DB
    # E o range, a gente pode criar uma variável pro usuário definir quantos jogos ele vai querer ver de uma vez
    ids_aleatorios = [random.randint(1000, 9999) for _ in range(1)]

    # Construa a string do corpo para obter os campos "name", "category" e "platforms"
    body_jogos = f"fields name, platforms, genres; where id = ({','.join(map(str, ids_aleatorios))});"

    # Aqui a gente ta basicamente criando uma variavel, que vai fazer o pedido pra api usando a biblioteca
    # "requests", dai ela puxa o metodo post, depois coloca os parametros, sendo a url,headers e o data que abrange o body
    resposta_jogos = requests.post(url_jogos, headers=headers, data=body_jogos)

    # Aqui é so a checagem pra ver se a solicitação deu bom ou não, esse 200 ta relacionado aos codigos http, dai tem o 200
    # 400 e tem mais alguns so que não fui atras kkkkk
    # O 200, significa que a solicitação deu bom, o 400 significa que deu merda no pedido
    if resposta_jogos.status_code == 200:
        data_jogos = resposta_jogos.json()

        # aqui é o processamento de dos dados, eu tenho que tirar essa categoria e a plataforma
        # mas quando eu tiro o negocio para de funcionar kkkkk, então tenho que ver melhor
        # aqui ele percorre a lista, e caso não tenha ele mete um NA e depois printa o nome do jogo
        for game in data_jogos:
            nome_jogo = game.get('name', 'N/A')
            plataformas = game.get('platforms', [])
            generos = game.get('genres', [])

            if generos:
                generos_info = []  # Remova esta linha para não redefinir a lista a cada iteração

                for genero_id in generos:
                    body_genero = f"fields name; where id = {genero_id};"
                    resposta_genero = requests.post(url_generos, headers=headers, data=body_genero)

                    if resposta_genero.status_code == 200:
                        genero_data = resposta_genero.json()

                        # Verifique se a resposta tem dados antes de acessar o primeiro elemento
                        if genero_data:
                            genero_nome = genero_data[0].get('name', 'N/A')
                            generos_info.append(genero_nome)
                        else:
                            generos_info.append('N/A')

            # Se houver plataformas, vai pegar e botar pra jogo kkkk
            if plataformas:
                plataformas_info = []

                for plataforma_id in plataformas:
                    body_plataforma = f"fields name; where id = {plataforma_id};"
                    resposta_plataforma = requests.post(url_plataformas, headers=headers, data=body_plataforma)

                    if resposta_plataforma.status_code == 200:
                        plataforma_data = resposta_plataforma.json()[0]
                        plataforma_nome = plataforma_data.get('name', 'N/A')
                        plataformas_info.append(plataforma_nome)
                # Imprima todas as informações de uma vez
                print(f"\nNome do Jogo: {nome_jogo}")
                print(f"\nGênero: {', '.join(generos_info)}")
                print(f"\nPlataformas: {', '.join(plataformas_info)}")

                nome = nome_jogo

            else:
                print(f"Nome do Jogo: {nome}, Plataformas: N/A")

        return nome, plataformas_info, generos_info

    else:
        print(f"Erro na solicitação de jogos: {resposta_jogos.status_code} - {resposta_jogos.text}")
