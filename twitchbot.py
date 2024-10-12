# twitch_bot.py
import os
from twitchio.ext import commands
from gtts import gTTS
import time

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
        
        # Generar el archivo de TTS usando Google TTS
        tts = gTTS(text, lang='es')
        tts.save("tts.mp3")
        
        # Manda la señal para iniciar la animación (esto puede ser vía websockets o un archivo)
        with open("trigger.txt", "w") as trigger:
            trigger.write("speak")
        
        # Reproducir el archivo en OBS
        os.system("start tts.mp3")
        
        await ctx.send(f"{ctx.author.name} dijo: {text}")

bot = Bot()
bot.run()
