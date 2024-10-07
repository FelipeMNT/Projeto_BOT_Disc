import requests

#Defina os valores do seu Client ID e Client Secret
client_id = "client id aqui"
client_secret = "client secret aqui"

#Parâmetros da solicitação
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

#Faça a solicitação POST para obter o token
url = "https://id.twitch.tv/oauth2/token"
response = requests.post(url, params=params)

#Verifique a resposta e obtenha o token de acesso, se for bem-sucedido
if response.status_code == 200:
    data = response.json()
    access_token = data.get("access_token")
    print(f"Token de acesso: {access_token}")
else:
    print(f"Erro na solicitação: {response.status_code} - {response.text}")