# Parte do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

# Reconhecimento de voz - speech recognition
import speech_recognition as sr

# speech synthesis
import pyttsx3

chatterbot = ChatBot('Lucas')

speak = pyttsx3.init('sapi5')


def speak_say(text):
    speak.say(text)
    speak.runAndWait()

chats = ['Oi', 'Olá', 'Como você está ?', 'Eu estou bem.', 'Obrigado.',
         'qual o seu nome ?', 'Lucas BOT', 'qual a sua cor favorita ?', 'Preto.', 'Qual o nome do seu criador?', 'Lucas Lamounier'] # conversas

chatterbot.set_trainer(ListTrainer) # define o metodo de treinamento
chatterbot.train(chats)
# define a lista de conversas
chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train(
    "chatterbot.corpus.portuguese"
)

r = sr.Recognizer()

# try:
#     with sr.Microphone() as s:
#         r.adjust_for_ambient_noise(s) # se adapta ao ruido
#         print('Say something: ')
#
#         while True:
#             try:
#                 audio = r.listen(s) # escutar
#                 speech = r.recognize_google(audio) # fala
#                 bot_response = chatterbot.get_response(speech)
#                 print('You: ', speech)
#                 print('Bot: ', bot_response)
#                 speak_say(bot_response)
#             except:
#                 print('Sorry..')
# except:
#     while True:
#         text = input('Entre com um texto: ')
#         print(chatterbot.get_response(text))


while True:
    text = input('Entre com um texto: ')
    print(chatterbot.get_response(text))




