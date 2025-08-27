import tkinter as tk
import ctypes
import ast

import helper

class Window:
    def __init__(self):
        self.self = self
        self.window = None
    
    #create the window instance
    def initiate(self):
        self.window = tk.Tk()

    #close the window instance to make things apply
    def close_loop(self):
        self.window.mainloop()

    #creates a frame within whatever window/frame is needed
    #
    # field -> the window/frame being added to
    # rows -> array of weights, for example 4 rows at 25% weight each is [25, 25, 25, 25], i = row
    # columns -> same as rows but applies to columns, eg [30, 70], i = column

    def new_frame(self):
        theme = helper.get_theme()
    
    #adds a title to the page
    def new_title_label(self):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = "Boombox")
        label.configure(activebackground = theme["highlight_colour"], bg= theme["background_colour"], bd = theme["border_width"], fg = theme["highlight_colour"], font=["title_font"])
        label.grid(row = 0, column = 0)

        return label
    
    #displays the version of the software
    def new_version_label(self):
        theme = helper.get_theme()
        version = helper.get_version()

        label = tk.Label(self.window, text = version)
        label.configure(activebackground = theme["highlight_colour"], bg= theme["background_colour"], bd = theme["border_width"], fg = theme["text_colour"], font=["version_font"])
        label.grid(row = 0, column = 1)

        return label


    #creates the basic window
    def format_window(self):
        #sets up the main window
        theme = helper.get_theme()
        dimensions = helper.get_dimensions()
    
        self.window.title("Boombox V1.0")
        self.window.geometry(dimensions)
        self.window.configure(background = theme["background_colour"])
        self.window.iconbitmap(default=theme["logo"])

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(theme["logo"])

        self.window.resizable(False, False)