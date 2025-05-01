import os
import eel
from engine.features import playAssistantSound

eel.init("www")

playAssistantSound()  # <- Function call corrected

# Open in app mode (Microsoft Edge)
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start("index.html", mode=None, host="localhost", block=True)
