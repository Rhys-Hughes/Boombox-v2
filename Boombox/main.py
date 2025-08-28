import tkinter as tk, helper

import UIManager as UIM

def debug():
    print("debug")

if __name__ == "__main__":

    #the main page everything happens on
    main_window = UIM.Window()
    main_window.initiate_page()
    main_window.format_page()
    main_window.format_rows_columns(rows = [2, 83, 5, 10])

    #title at the top of the main page
    title_frame = UIM.Window()
    title_frame.initiate_frame(parent = main_window.window, grid = (0,0))
    title_frame.new_title_label(content = "Boombox")
    title_frame.new_version_label()

    #sound frame where the contents of the sounboard is stored
    sound_frame = UIM.Window()
    sound_frame.initiate_frame(parent = main_window.window, grid = (0,1))
    sound_frame.format_rows_columns(rows = [3, 97])

    #microphone control frame
    mic_frame = UIM.Window()
    mic_frame.initiate_frame(parent = main_window.window, grid = (0,2))
    mic_frame.format_rows_columns(rows = [50, 50], columns = [80, 20])

    #editing frame where the user has access to settings and such
    editing_frame = UIM.Window()
    editing_frame.initiate_frame(parent = main_window.window, grid = (0, 3))
    editing_frame.format_rows_columns(columns = [50, 50])


    #----------------------------------------------------------------------------------populating the sound frame
    sound_frame.new_label(content = "sounds", grid = (0, 0))

    content_frame =UIM.Window()
    content_frame.initiate_scrollable_frame(parent = sound_frame.window, grid = (0, 1))
    content_frame.format_rows_columns(columns = [60, 20, 10, 10], only = True)

    #filling th econtent frame
    sound_list = helper.get_sound_list()
    
    #adding each sound from the sound list to the content frame
    for i, sound in enumerate(sound_list):

        #name of the sound
        content_frame.new_neutral_label(content = sound.name, grid = (0, i), sticky = "sticky")

        #keybind of the sound
        content_frame.new_neutral_label(content = helper.get_keybind_string(sound.keybind), grid = (1, i), sticky = "sticky")

        #settings to edit the sound
        content_frame.new_button(content = "⚙", grid = (2, i), sticky = "sticky")

        #play button to manually play the sound
        content_frame.new_button(content = "▶", grid = (3, i), sticky = "sticky")



    main_window.close_loop()