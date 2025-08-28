import sounddevice as sd
import soundfile as sf
import ast
import keyboard
import time
import numpy as np
from threading import Thread
import os


def play(file):
    print(file)