import discord
import respostas
import requests 

async def enviar_mesnagem(message, mensagem_usuario, is_private):
    try:
        resposta = respostas.receber_resposta(mensagem_usuario)
        await message.author.send(resposta) if is_private else await message.channel.send(resposta)
    
    except Exception as e:
        print(e)

def solicitar_igdb(api_endpoint, access_token):
    # Defina o cabeçalho com o Client-ID e o token de acesso
    headers = {
        "Client-ID": "client id aqui",
        "Authorization": f"Bearer {access_token}"
    }

    # Monte a URL da solicitação
    base_url = "https://api.igdb.com/v4/"
    url = base_url + api_endpoint

    # Defina os campos e outros parâmetros no corpo da solicitação
    body = "fields *; limit 10;"

    # Faça a solicitação POST à API da IGDB
    response = requests.post(url, headers=headers, data=body)

    # Verifique a resposta e retorne os dados ou trate os erros
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro na solicitação à API da IGDB: {response.status_code} - {response.text}")
        return None

def rodar_bot():
    token = "token aqui"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"O bot {client.user} está finalmente vivo!!")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        usuario = str(message.author)
        mensagem_usuario = str(message.content)
        channel = str(message.channel)

        print(f'{usuario} disse: "{mensagem_usuario}" ({channel})')

        if mensagem_usuario[0] == "!":
            mensagem_usuario = mensagem_usuario[1:]
            await enviar_mesnagem(message, mensagem_usuario, is_private=True)
        else:
            await enviar_mesnagem(message, mensagem_usuario, is_private=False)

    client.run(token)




