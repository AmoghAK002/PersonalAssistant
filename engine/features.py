from playsound import playsound
import eel

# playing sound of jarvis
@eel.expose
def playAssistantSound():
    music_dir = r"www\\assets\\audio\\alice39s-sound-yandex-voice-assistant.mp3"
    playsound(music_dir, True)
