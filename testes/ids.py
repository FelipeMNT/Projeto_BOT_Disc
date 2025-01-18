import requests
import random

client_id = "4elq3ap5bbx9k0miiawydrgcwunyqe"
access_token = "1impvz5olht4gz7gra11d5e77hs6b8"

url_jogos = "https://api.igdb.com/v4/games/"
url_generos = "https://api.igdb.com/v4/genres/"

headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}"
}

ids_aleatorios = [random.randint(0, 99999) for _ in range(30)]

body_jogos = f"fields name, platforms, genres; where id = ({','.join(map(str, ids_aleatorios))});"
body_genero = f"fields checksum,created_at,name,slug,updated_at,url;"

resposta_jogos = requests.post(url_jogos, headers=headers, data=body_jogos)

if resposta_jogos.status_code == 200:
    data_games = resposta_jogos.json()

    for game in data_games:
        nome = game.get('name', 'N/A')
        id_gen = game.get('genres', [])

        if id_gen:
            generos_info = []  # Remova esta linha para não redefinir a lista a cada iteração

            for genero_id in id_gen:
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

            print(f"Nome: {nome}\nGênero: {generos_info}\nID: {id_gen}\n")

else:
    print("deu merda")