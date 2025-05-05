import os
import re
import struct
import eel
import pvporcupine
import pyaudio
import pyttsx3
import webbrowser
from playsound import playsound
import pywhatkit as kit
from engine.db import cursor  
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term
import time

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 174)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function
def speak(text):
    print("Assistant:", text)
    try:
        eel.DisplayMessage(text)
    except:
        pass
    engine.say(text)
    engine.runAndWait()

# Play assistant startup sound
@eel.expose
def playAssistantSound():
    music_dir = r"www\\assets\\audio\\alice39s-sound-yandex-voice-assistant.mp3"
    if os.path.exists(music_dir):
        playsound(music_dir)
    else:
        speak("Sound file not found.")

# Open application or web link


@eel.expose
def openCommand(query):
    query = query.replace(ASSISTANT_NAME.lower(), "")
    query = query.replace("open", "").strip().lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name = ?", (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute("SELECT path FROM web_command WHERE name IN (?)", (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + query)
                    try:
                        os.system("start " + query)
                    except:
                        speak("Sorry, I couldn't find the application or website you requested.")
        except:
            speak("Sorry, I couldn't find the application or website you requested.")


# Play YouTube video
@eel.expose
def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I couldn't understand what you said!.")

 
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()