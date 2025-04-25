from core.wake_word import detect_wake_word
from core.speech_to_text import recognize_speech
from core.text_to_speech import speak
from core.intent_handler import handle_intent

def assistant_logic():
    query = recognize_speech()
    if query:
        print(f"[You]: {query}")
        response = handle_intent(query)
        speak(response)
    else:
        speak("Sorry, I didn't catch that.")

if __name__ == "__main__":
    detect_wake_word(assistant_logic)
