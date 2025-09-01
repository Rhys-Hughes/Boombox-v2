import sounddevice as sd
import soundfile as sf
import ast
import keyboard
import time
import numpy as np
from threading import Thread
import os
import helper

global volume
volume = 1
global micLevel
micLevel = 0

#plays a specific file
def play(file):

    try:
        data, samplerate = sf.read(file, dtype='float32')

        sd.play(data, samplerate=samplerate, blocking = False)
        sd.wait()

    except:
        pass

#callback function used by the input stream
def callback(indata, outdata, frames, time, status):
    global micLevel
    outdata[:] = indata * volume
    micLevel = np.mean(indata)

#establishes the minimum devices and stream
def initialise_audio():

    input_device, output_device, sample_rate, host_api = helper.get_IO_defaults()

    #if there are default input and outputs
    if input_device == "" or output_device == "" or sample_rate == "" or host_api == "":




        # --- TO BE REPLACED WITH A UI BASED SOLUTION --- #

        print(sd.query_devices())

        input_index= int(input("INPUT>>>"))
        output_index = int(input("OUTPUT>>>"))
        
        #creating the new default input and outputs and setting them into a list of their names
        new_default_input = sd.query_devices(input_index)
        new_default_output = sd.query_devices(output_index)

        devices_dictionary = {
                                "input" : new_default_input["name"],
                                "output" : new_default_output["name"],
                                "sample_rate" : new_default_input["default_samplerate"],
                                "host_api" : new_default_input["hostapi"]
                             }

        #file re-written
        helper.write_IO_defaults(devices_dictionary)
    
    else:
        device_list = sd.query_devices()

        #enumerates through the devices we have just queried, and checks if they have names matching the default input and output devices
        for index, device in enumerate(device_list):

            #if the names match, the index of the respective device is set to the index we want
            if device["name"] == input_device and device["default_samplerate"] == sample_rate and device["hostapi"] == host_api:
                input_index = index

            if device["name"] == output_device and device["default_samplerate"] == sample_rate and device["hostapi"] == host_api:
                output_index = index

    try:
        #defualt devices set
        sd.default.device = (input_index, output_index)

        stream = sd.Stream(callback=callback)
        stream.start()

    
    except Exception as e:

        # --- TO BE REPLACED WITH A UI BASED SOLUTION --- #

        print(e)

#sets the microphone volume at a certain level
def set_mic_volume(volume_new):
    global volume
    volume = volume_new

#returns the current mic volume
def get_mic_level():
    global micLevel
    level = abs(micLevel * 1000)
    
    if level < 0.09:
        return 0
    else:
        return level

#mutes and unmutes the microphone
def mute_unmute_mic():
    pass