import os
import eel
from engine.features import *
from engine.command import *

def start():
    eel.init("www")
    eel.start("index.html", size=(800, 600))
    eel.init("www")

    playAssistantSound()

    # Open in app mode using Edge
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start("index.html", mode=None, host="localhost", block=True)
