import os
from twitchio.ext import commands
from gtts import gTTS

# Crea tu bot de Twitch
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='TU_TOKEN_OAUTH', prefix='!', initial_channels=['TU_CANAL'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command(name='speak')
    async def speak(self, ctx):
        # Obtener el mensaje a convertir en TTS
        text = ctx.content[len('!speak '):]

        if text:
            # Generar el archivo de TTS usando Google TTS
            tts = gTTS(text, lang='es')
            tts.save("tts.mp3")
            
            # Manda la señal para iniciar la animación (escribiendo en trigger.txt)
            with open("trigger.txt", "w") as trigger:
                trigger.write("speak")
            
            # Reproduce el archivo en OBS (opcional: depende de cómo lo estés integrando)
            os.system("start tts.mp3")
            
            # Enviar mensaje al chat confirmando
            await ctx.send(f"{ctx.author.name} dijo: {text}")
        else:
            await ctx.send(f"{ctx.author.name}, debes proporcionar un mensaje después del comando !speak.")

bot = Bot()
bot.run()
