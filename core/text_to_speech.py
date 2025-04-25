import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Optional: change speaking speed

def speak(text):
    print(f"[Assistant]: {text}")
    engine.say(text)
    engine.runAndWait()
