# BBot-2 

# https://github.com/Harish-ioc/BBot-2


# from Main.py file

import time
import threading
from calling import ask
from thread1 import watch
from Google_speech_to_text import listen
# from eleven_labs import speak


pause_event = threading.Event()
pause_event.set()

# while True:
trigger = ["Hello","Hi there","Hey","Greetings","Good morning","Good afternoon","Good evening","Howdy","Yo","What's up","Hiya",
            "Hola","Bonjour","Ciao","Namaste","Salaam","Good day","Shalom","Aloha","Konnichiwa"]

closing = ["Goodbye","Farewell","See you later","Take care","Adios","Sayonara","Cheerio","Till we meet again","Catch you later","So long",
        "Bye bye","Auf Wiedersehen","Arrivederci","Hasta luego","Until next time","Thanks","Thank you","Thanks a lot","Thank you very much","Appreciate it","Much obliged",
        "Gracias","Arigato","Merci","Domo arigato","Cheers","See you soon","Take it easy"]
