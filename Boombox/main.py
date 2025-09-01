import tkinter as tk, helper

import UIManager as UIM
import audioManager as AM

def debug(val):
    print(val)

if __name__ == "__main__":

    #the main page everything happens on
    main_window = UIM.Window()
    main_window.initiate_page()
    main_window.format_page()
    main_window.format_rows_columns(rows = [2, 100, 5, 5, 5, 5])

    #title at the top of the main page
    title_frame = UIM.Window()
    title_frame.initiate_frame(parent = main_window.window, grid = (0,0), sticky = "sticky")
    title_frame.new_label(style = "title", content = "Boombox")
    title_frame.new_label(style = "version")

    #sound frame where the contents of the sounboard is stored
    sound_frame = UIM.Window()
    sound_frame.initiate_frame(parent = main_window.window, grid = (0,1), sticky = "sticky")
    sound_frame.format_rows_columns(rows = [3, 97])

    #microphone control frame
    mic_frame = UIM.Window()
    mic_frame.initiate_frame(parent = main_window.window, grid = (0,2), sticky = "sticky")
    mic_frame.format_rows_columns(rows = [50, 50], columns = [80, 20])

    mic_mute_frame = UIM.Window()
    mic_mute_frame.initiate_frame(parent = main_window.window, grid = (0,3), sticky = "sticky")
    mic_mute_frame.format_rows_columns(columns = [50, 50])

    #editing frame where the user has access to settings and such
    editing_frame = UIM.Window()
    editing_frame.initiate_frame(parent = main_window.window, grid = (0, 4), sticky = "sticky")
    editing_frame.format_rows_columns(columns = [50, 50])



    #----------------------------------------------------------------------------------populating the sound frame
    def sound_settings_popout():
        pass

    sound_frame.new_label(style = "standard", content = "sounds", grid = (0, 0))

    content_frame = UIM.Window()
    content_frame.initiate_scrollable_frame(parent = sound_frame.window, grid = (0, 1))
    content_frame.format_rows_columns(columns = [60, 20, 10, 10], only = True)
    content_frame.format_frame_border(scrollable = True)

    #filling th econtent frame
    sound_list = helper.get_sound_list()
    
    #adding each sound from the sound list to the content frame
    for i, sound in enumerate(sound_list):

        #name of the sound
        content_frame.new_label(style = "neutral", content = sound.name, grid = (0, i), sticky = "sticky", xyBuffer = (2, 2))

        #keybind of the sound
        content_frame.new_label(style = "neutral", content = helper.get_keybind_string(sound.keybind), grid = (1, i), sticky = "sticky", xyBuffer = (2, 2))

        #settings to edit the sound
        content_frame.new_button(style = "neutral", content = "⚙", grid = (2, i), sticky = "sticky", xyBuffer = (2, 2), command = sound_settings_popout)

        #play button to manually play the sound
        content_frame.new_button(style = "neutral", content = "▶", grid = (3, i), sticky = "sticky", xyBuffer = (2, 2), command = sound.play)



    #----------------------------------------------------------------------------------creating the mic controls
    mic_frame.new_label(style = "standard", content = "Mic Vol", grid = (0, 0))
    mic_frame.new_slider(10, grid = (1, 0))

    mic_frame.new_label(style = "standard", content = "level", grid = (0, 1))
    mic_frame.new_volume_bar(grid = (1,1))


    mic_mute_frame.new_label(style = "standard", content = "mute / unmute", grid = (0, 0), sticky = "sticky")
    mic_mute_frame.new_button(style = "highlight", content = "🎤", grid = (1, 0), sticky = "sticky", command = AM.mute_unmute_mic)



    #----------------------------------------------------------------------------------settings
    def settings_popout():
        pass

    def add_sound_popout():
        pass

    editing_frame.new_button(style = "highlight", content = "settings", grid = (0, 0), command = settings_popout)
    editing_frame.new_button(style = "highlight", content = "add sound", grid = (1, 0), command = add_sound_popout)


    AM.initialise_audio()

    main_window.close_loop()