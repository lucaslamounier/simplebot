from gtts import gTTS
import subprocess as s

voz = gTTS("Hello")
voz.save("voz.mp3")

voz = gTTS("Olá, tudo bem?")
voz.save("ola.mp3")

voz = gTTS("Olá, tudo bem?", lang="pt")
voz.save("ola.mp3")