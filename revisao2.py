from gtts import gTTS
from playsound import playsound

audio = gTTS('Bom dia', lang='pt')
audio.save('cumprimento.mp3')

playsound('cumprimento.mp3')
