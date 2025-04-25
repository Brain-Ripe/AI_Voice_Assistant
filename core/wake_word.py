import pvporcupine
import sounddevice as sd
import struct

def detect_wake_word(callback):
    porcupine = pvporcupine.create(
        access_key="yKpLYp8DqrJGMz5Kv5fuJdQyJyTyT+ts+3/TLqxd8HSgetqgRYeE1w==",  # Replace this
        keyword_paths=["assets/Lotus_en_windows.ppn"]  # Update with your actual file
    )

    def audio_callback(indata, frames, time, status):
        if status:
            print(status)
        pcm = struct.unpack_from("h" * porcupine.frame_length, indata[0])
        result = porcupine.process(pcm)
        if result >= 0:
            print("[Wake Word Detected]")
            callback()

    with sd.InputStream(channels=1, samplerate=porcupine.sample_rate,
                        blocksize=porcupine.frame_length,
                        dtype='int16',
                        callback=audio_callback):
        print("Listening for wake word...")
        while True:
            sd.sleep(1000)
