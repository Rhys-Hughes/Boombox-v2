import tkinter as tk
import ctypes
import ast

import helper

class Window:
    def __init__(self):
        self.self = self
    
    def initiate(self):

        theme = helper.get_theme()
        dimensions = helper.get_dimensions()

        #sets up the main window
        window = tk.Tk()

        self.format_window(window)
        
        title = self.new_title_label(window)
        version = self.new_version_label(window)

        window.mainloop()
    



    def new_frame(self, window, rows, ):
        theme = helper.get_theme()
    
    #adds a title to the page
    def new_title_label(self, window):
        theme = helper.get_theme()

        label = tk.Label(window, text = "Boombox")
        label.configure(activebackground = theme["highlight_colour"], bg= theme["background_colour"], bd = theme["border_width"], fg = theme["highlight_colour"], font=["title_font"])
        label.grid(row = 0, column = 0)

        return label
    
    #displays the version of the software
    def new_version_label(self, window):
        theme = helper.get_theme()
        version = helper.get_version()

        label = tk.Label(window, text = version)
        label.configure(activebackground = theme["highlight_colour"], bg= theme["background_colour"], bd = theme["border_width"], fg = theme["text_colour"], font=["version_font"])
        label.grid(row = 0, column = 1)

        return label


    #creates the basic window
    def format_window(self, window):
        #sets up the main window
        theme = helper.get_theme()
        dimensions = helper.get_dimensions()
    
        window.title("Boombox V1.0")
        window.geometry(dimensions)
        window.configure(background = theme["background_colour"])
        window.iconbitmap(default=theme["logo"])

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(theme["logo"])

        window.resizable(False, False)