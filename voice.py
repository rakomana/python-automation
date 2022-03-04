import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 0.1)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    text = input("Enter text you want say: ")
    engine.say(f'{text}')

    engine.runAndWait()

