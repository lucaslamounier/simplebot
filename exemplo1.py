import pyttsx

engine = pyttsx.init()
engine.say("hello")
engine.runAndWait()
engine.say("Meu nome é lucas lamounier")
engine.runAndWait()
engine.setProperty('voice', b'brazil')
engine.say("Olá, tudo bem?")
engine.runAndWait()