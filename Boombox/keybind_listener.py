import keyboard
from threading import Thread
import helper
import time

def listen(sound_list):
    
    while True:
        for i, sound in enumerate(sound_list):
   
            if all(keyboard.is_pressed(key) for key in sound.keybind):

                sound.play()
                print(sound.name)

                time.sleep(1)
        
        time.sleep(0.01)

def initiate_keybind_listener():
    sound_list = helper.get_sound_list()

    #for some reason if i don't put a comma after "sound_list" it breaks, will have to fix
    listen_thread = Thread(target = listen, args = (sound_list,), daemon = True)
    listen_thread.start()