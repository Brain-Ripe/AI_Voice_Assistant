import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\Parthav\Desktop\Project\AI Assistant\models\vosk-model")

def recognize_speech(duration=8):
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = KaldiRecognizer(model, 16000)
        print("Listening...")
        result_text = ""

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                result_text = result.get("text", "")
                break

        return result_text
