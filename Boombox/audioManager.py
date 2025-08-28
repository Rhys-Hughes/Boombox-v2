import sounddevice as sd
import soundfile as sf
import ast
import keyboard
import time
import numpy as np
from threading import Thread
import os

#plays a specific file
def play(file):
    print(file)

#sets the microphone volume at a certain level
def set_mic_volume(volume):
    return volume

#returns the current mic volume
def get_mic_volume():
    return 50