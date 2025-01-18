import requests
import random

# Substitua esses valores pelos seus dados
client_id = "4elq3ap5bbx9k0miiawydrgcwunyqe"
access_token = "1impvz5olht4gz7gra11d5e77hs6b8"
url_games = "https://api.igdb.com/v4/games/"
url_platforms = "https://api.igdb.com/v4/platforms/"

# Cabeçalhos da solicitação
headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}"
}

# Gerando IDs aleatórios de jogos
random_game_ids = [random.randint(1000, 9999) for _ in range(1)]

# Construindo o corpo da solicitação para detalhes de jogos
body_games = f"fields name, platforms; where id = ({','.join(map(str, random_game_ids))});"

# Fazendo solicitação POST para detalhes de jogos
response_games = requests.post(url_games, headers=headers, data=body_games)

# Processando Dados dos Jogos
if response_games.status_code == 200:
    data_games = response_games.json()

    for game in data_games:
        nome = game.get('name', 'N/A')
        plataformas = game.get('platforms', [])

        # Se houver plataformas, colete as informações
        if plataformas:
            plataformas_info = []

            for plataforma_id in plataformas:
                body_platform = f"fields name; where id = {plataforma_id};"
                response_platform = requests.post(url_platforms, headers=headers, data=body_platform)

                if response_platform.status_code == 200:
                    plataforma_data = response_platform.json()[0]
                    plataforma_nome = plataforma_data.get('name', 'N/A')
                    plataformas_info.append(plataforma_nome)

            # Imprima todas as informações de uma vez
            print(f"Nome do Jogo: {nome}, \nPlataformas: {', '.join(plataformas_info)}")

        else:
            print(f"Nome do Jogo: {nome}, Plataformas: N/A")

    # Tratamento de Erros para a Solicitação de Jogos
else:
    print(f"Erro na solicitação de jogos: {response_games.status_code} - {response_games.text}")