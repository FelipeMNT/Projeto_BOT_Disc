import discord
import respostas


async def enviar_mensagem(message, mensagem_usuario, is_private):
    try:
        resposta = respostas.receber_resposta(mensagem_usuario)
        await message.author.send(resposta) if is_private else await message.channel.send(resposta)

    except Exception as e:
        print(e)


def rodar_bot():
    token = "TOKEN DO DISCORD DEVELOPER"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"O bot {client.user} está finalmente vivo!!\n")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        usuario = str(message.author)
        mensagem_usuario = str(message.content)
        canal = str(message.channel)

        print(f'Usuário: {usuario} \nDisse: "{mensagem_usuario}" \nCanal: ({canal})')

        if mensagem_usuario[0] == "!":
            mensagem_usuario = mensagem_usuario[1:]
            await enviar_mensagem(message, mensagem_usuario, is_private=True)
        else:
            await enviar_mensagem(message, mensagem_usuario, is_private=False)

    client.run(token)