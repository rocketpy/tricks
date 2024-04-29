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

def vision():
    print("1")
    while True:
        # print("Loop 1 is running")
        watch()
        time.sleep(0.08)  # Simulate some work
        pause_event.wait()

def talk():
    print("2")
    while True:
        print("Loop 2 is running")
        que = listen()

        # print(ask(str(que)))

        # --- conditions ---

        if any(str(item) in que for item in trigger):
            print("3")
            # pause_event.clear()   # pause other threads 
            reply=ask(str(que))
            # pause_event.set()     # continue other threads 

            print(reply)
            # speak(reply)

            # continue listening ---
            while True:
                print("4")
                que = listen()

                if any(str(item) in que for item in closing):
                    print("5")
                    # pause_event.clear()
                    reply= ask(str(que))
                    # pause_event.set()
                    
                    print(reply)
                    # speak(reply)
                    break

                # pause_event.clear()
                ans = ask(str(que))
                # pause_event.set()

                print(ans)


    # speak(str(ans))
        time.sleep(0.01)  # Simulate some work

# camera - face detect - position 
#  listen - txt - check -  ask - speak
