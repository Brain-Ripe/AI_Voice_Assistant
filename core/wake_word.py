import pvporcupine
import sounddevice as sd
import struct

def detect_wake_word(callback):
    while True:  # <-- Add a loop to always listen
        porcupine = pvporcupine.create(
            access_key="yKpLYp8DqrJGMz5Kv5fuJdQyJyTyT+ts+3/TLqxd8HSgetqgRYeE1w==",
            keyword_paths=["assets/Lotus_en_windows.ppn"]
        )

        def audio_callback(indata, frames, time, status):
            if status:
                print(status)
            pcm = struct.unpack_from("h" * porcupine.frame_length, indata.tobytes())
            result = porcupine.process(pcm)
            if result >= 0:
                print("[Wake Word Detected]")
                callback()

        try:
            with sd.InputStream(
                samplerate=porcupine.sample_rate,
                blocksize=porcupine.frame_length,
                channels=1,
                dtype='int16',
                callback=audio_callback):
                
                print("Listening for wake word...")
                while True:
                    sd.sleep(1000)  # keep sleeping while stream is active
        except Exception as e:
            print(f"Error: {e}")
        finally:
            porcupine.delete()  # clean up before restarting

