import pvporcupine
import sounddevice as sd
import struct
import time
import threading
import winsound   # <-- new for playing beep sound

def play_beep():
    winsound.Beep(1000,200)

def detect_wake_word(callback):
    while True:
        porcupine = pvporcupine.create(
            access_key="yKpLYp8DqrJGMz5Kv5fuJdQyJyTyT+ts+3/TLqxd8HSgetqgRYeE1w==",
            keyword_paths=["assets/Lotus_en_windows.ppn"]
        )

        wake_word_detected = False
        start_time = time.time()

        def audio_callback(indata, frames, time_info, status):
            nonlocal wake_word_detected
            if status:
                print(status)
            pcm = struct.unpack_from("h" * porcupine.frame_length, indata.tobytes())
            result = porcupine.process(pcm)
            if result >= 0:
                print("[Wake Word Detected]")
                wake_word_detected = True

        try:
            with sd.InputStream(
                samplerate=porcupine.sample_rate,
                blocksize=porcupine.frame_length,
                channels=1,
                dtype='int16',
                callback=audio_callback):
                
                print("Listening for wake word...")

                while True:
                    sd.sleep(100)

                    if wake_word_detected:
                        play_beep()  # <-- play the beep immediately!
                        threading.Thread(target=callback).start()
                        break

                    if time.time() - start_time > 10:
                        print("[Timeout] No wake word detected. Restarting...")
                        break

        except Exception as e:
            print(f"Error: {e}")

        finally:
            porcupine.delete()
