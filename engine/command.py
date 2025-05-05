import speech_recognition as sr
import eel
import time
from engine.features import openCommand, playYoutube, speak

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        eel.DisplayMessage(query)
        time.sleep(1)
        return query.lower()
    except Exception as e:
        print(f"Recognition failed: {e}")
        eel.DisplayMessage("Sorry, I didn't catch that.")
        return ""

@eel.expose
def allCommands():
    try:
        query = takecommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import playYoutube
            playYoutube(query)
        else:
            print("Command not recognized")
    except:
        print("Error")
    
    eel.ShowHood()
