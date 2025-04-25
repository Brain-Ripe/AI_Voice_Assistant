import os

def handle_system_commands(text):
    text = text.lower()

    if "open browser" in text or "start browser" in text:
        os.system("start chrome")
        return "Opening Chrome browser."

    elif "open notepad" in text:
        os.system("start notepad")
        return "Opening Notepad."

    elif "volume up" in text:
        os.system("nircmd.exe changesysvolume 2000")
        return "Turning up the volume."

    elif "volume down" in text:
        os.system("nircmd.exe changesysvolume -2000")
        return "Turning down the volume."

    elif "mute" in text:
        os.system("nircmd.exe mutesysvolume 1")
        return "Muting the system."

    elif "unmute" in text:
        os.system("nircmd.exe mutesysvolume 0")
        return "Unmuting the system."

    else:
        return "Sorry, I didn't understand the system command."
