import sounddevice as sd
import soundfile as sf
import numpy as np
from threading import Thread
import helper

global volume
volume = 1
global micLevel
micLevel = 0
global last_volume
last_volume = 1

#plays a specific file
def play(file):

    #making the play stream multi threaded eliminates the issue of having the application freeze upon playing a sound.
    #this does not allow you to speak and play sounds at the same time, however it does mean you can still play long
    #sounds without freezing the application for several seconds
    def play_file():
        try:

            data, samplerate = sf.read(file, dtype='float32')

            sd.play(data, samplerate=samplerate, blocking = False)
            sd.wait()

        except Exception as e:
            print(e)

        
    play_thread = Thread(target = play_file, daemon = True)
    play_thread.start()



#callback function used by the input stream
def callback(indata, outdata, frames, time, status):
    global micLevel
    outdata[:] = indata * volume
    micLevel = np.mean(indata)

#establishes the minimum devices and stream
def initialise_audio():

    input_device, output_device, sample_rate, host_api, playback_device = helper.get_IO_defaults()

    #if there are default input and outputs
    if input_device == "" or output_device == "" or sample_rate == "" or host_api == "" or playback_device == "":

        # --- TO BE REPLACED WITH A UI BASED SOLUTION --- #
        
        device_list = sd.query_devices()

        #print the input devices
        for i, device in enumerate(device_list):
            
            #looking for input devices
            if device["max_output_channels"] == 0:
                print(str(device["index"]) + " -> " + device["name"])

        #allow a user to select
        input_index= int(input("INPUT>>>"))

        #sets the sample rate and host api needed so that the output devices match
        template_device_info = {
                "sample_rate" : "",
                "host_api" : ""
        }

        template_device = device_list[input_index]
        template_device_info["sample_rate"] = template_device["default_samplerate"]
        template_device_info["host_api"] = template_device["hostapi"]


        for i, device in enumerate(device_list):
            
            #looking for output devices
            if device["max_input_channels"] == 0 and device["default_samplerate"] == template_device_info["sample_rate"] and device["hostapi"] == template_device_info["host_api"]:
                print(str(device["index"]) + " -> " + device["name"])

        output_index = int(input("OUTPUT (VB CABLE)>>>"))
        playback_index = int(input("PLAYBACK OUTPUT>>>"))
        


        #creating the new default input and outputs and setting them into a list of their names
        new_default_input = sd.query_devices(input_index)
        new_default_output = sd.query_devices(output_index)
        new_default_playback_output = sd.query_devices(playback_index)

        devices_dictionary = {
                                "input" : new_default_input["name"],
                                "output" : new_default_output["name"],
                                "sample_rate" : new_default_input["default_samplerate"],
                                "host_api" : new_default_input["hostapi"],
                                "playback_output" : new_default_playback_output["name"]
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
            
            if device["name"] == playback_device and device["default_samplerate"] == sample_rate and device["hostapi"] == host_api:
                playback_index = index

    try:
        #defualt devices set
        sd.default.device = (input_index, output_index)

        stream = sd.Stream(callback=callback)
        stream.start()    

        #print("### main stream established ###")

    except Exception as e:

        # --- TO BE REPLACED WITH A UI BASED SOLUTION --- #

        print(e)

    try:
        # code that establishes a playback stream, currently not working as intended so is being left
        if False:
            settings = helper.get_settings()
            if settings["playback"] == "true":

                playback_stream = sd.Stream(callback = callback, device = (output_index, playback_index))
                playback_stream.start()
            
                #print("### playback stream established ###")

    except Exception as e:
        print(e)

#sets the microphone volume at a certain level
def set_mic_volume(volume_new):
    global volume
    volume = volume_new

#returns the current mic volume
def get_mic_level():
    global micLevel
    global volume
    level = abs(micLevel * volume* 1000)
    
    if level < 0.09:
        return 0
    else:
        return level

#mutes and unmutes the microphone
def mute_unmute_mic():
    global last_volume
    global volume

    if volume != 0:
        last_volume = volume
        volume = 0
    elif volume == 0:
        volume = last_volume