import requests

# Substitua esses valores pelos seus dados
client_id = "4elq3ap5bbx9k0miiawydrgcwunyqe"
client_secret = "k0zzy7766labhixs4a8ra71t8399wx"

# Construa os parâmetros da solicitação
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# Faça a solicitação POST
response = requests.post("https://id.twitch.tv/oauth2/token", params=params)

# Verifique a resposta
if response.status_code == 200:
    data = response.json()
    access_token = data["access_token"]
    expires_in = data["expires_in"]
    token_type = data["token_type"]
    print(f"Access Token: {access_token}\nExpires In: {expires_in} seconds\nToken Type: {token_type}")
else:
    print(f"Erro na solicitação: {response.status_code} - {response.text}")
