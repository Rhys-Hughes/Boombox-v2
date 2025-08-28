import tkinter as tk
import ctypes
import customtkinter as ctk

import helper, audioManager

class Window:
    def __init__(self):
        self.self = self
        self.window = None
    
    #create the window instance
    def initiate_page(self):
        self.window = tk.Tk()
    
    #creates a new frame within the UI
    #
    # parent -> parent frame/page
    # grid -> tuple coordinades as (column, row)
    # sticky -> makes the frame fill the grid area it is in
    def initiate_frame(self, parent, grid = None, sticky = None):
        theme = helper.get_theme()
        self.window = tk.Frame(parent)

        if sticky == "not sticky":
            if grid is None:
                self.window.pack()
            else:
                self.window.grid(row = grid[1], column = grid[0])
        else:
            if grid is None:
                self.window.pack()
            else:
                self.window.grid(row = grid[1], column = grid[0], sticky = "nsew")
        
        self.window.configure(bg = theme["background_colour"])
    
    #creates a new frame within the UI
    #
    # parent -> parent frame/page
    # grid -> tuple coordinades as (column, row)
    # sticky -> makes the frame fill the grid area it is in
    def initiate_scrollable_frame(self, parent, grid = None, sticky = None):
        theme = helper.get_theme()
        self.window = ctk.CTkScrollableFrame(parent)

        if sticky == "not sticky":
            if grid is None:
                self.window.pack()
            else:
                self.window.grid(row = grid[1], column = grid[0])
        else:
            if grid is None:
                self.window.pack()
            else:
                self.window.grid(row = grid[1], column = grid[0], sticky = "nsew")

        self.window.configure(fg_color = theme["background_colour"], 
                              border_color = theme["highlight_colour"], 
                              border_width = theme["border_width"], 
                              scrollbar_button_color = theme["highlight_colour"], 
                              scrollbar_button_hover_color = theme["highlight_colour"])

    #close the window instance to make things apply
    def close_loop(self):
        self.window.mainloop()    




    #formats the page
    def format_page(self):
        #sets up the main window
        theme = helper.get_theme()
        dimensions = helper.get_dimensions()
    
        self.window.title("Boombox V1.0")
        self.window.geometry(dimensions)
        self.window.configure(background = theme["background_colour"])
        self.window.iconbitmap(default=theme["logo"])

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(theme["logo"])

        self.window.resizable(False, False)

    #creates a frame within whatever window/frame is needed
    #
    # rows -> array of weights, for example 4 rows at 25% weight each is [25, 25, 25, 25], i = row
    # columns -> same as rows but applies to columns, eg [30, 70], i = column
    def format_rows_columns(self, rows = None , columns = None, only = None):

        if rows is None:
            if only is None:
                self.window.rowconfigure(0, weight = 100)
        else:
            for i, row_weight in enumerate(rows):
                self.window.rowconfigure(i, weight = row_weight)

        
        if columns is None:
            if only is None:
                self.window.columnconfigure(0, weight = 100)
        else:
            for i, column_weight in enumerate(columns):
                self.window.columnconfigure(i, weight = column_weight)
    
    def format_frame_border(self, scrollable = None):
        theme = helper.get_theme()

        if scrollable == True:
            self.window.configure(border_color = theme["highlight_colour"], border_width = theme["frame_border_width"])
        else:
            self.window.configure(highlightcolor = theme["highlight_colour"], highlightthickness= theme["frame_border_width"])



    #adds a title to the page
    #
    # content -> string of Content
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    # sticky -> if "not sticky" the widget will not be sticky
    # xyBuffer -> touple which creates a buffer as (x, y)
    def new_title_label(self, content, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["highlight_colour"], 
                        font=theme["title_font"])

        if xyBuffer is not None:
            label.configure(padx = xyBuffer[0], pady = xyBuffer[1])
        
        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label
    
    def new_version_label(self, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()
        version = helper.get_version()

        label = tk.Label(self.window, text = version)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["text_colour"], 
                        font=theme["version_font"])
        
        if xyBuffer is not None:
            label.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    def new_label(self, content, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["text_colour"], 
                        font=theme["standard_font"])
        
        if xyBuffer is not None:
            label.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    def new_neutral_label(self, content, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["neutral_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["background_colour"], 
                        font=theme["standard_font"])
        
        if xyBuffer is not None:
            label.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    def new_button(self, content, grid = None, command = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        if command is None:
            button = tk.Button(self.window, text = content)
        else:
            button = tk.Button(self.window, text = content, command = command)

        button.configure(activebackground = theme["highlight_colour"], 
                         bg= theme["background_colour"], 
                         bd = theme["border_width"], 
                         fg = theme["text_colour"], 
                         font=theme["standard_font"])

        if xyBuffer is not None:
            button.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                button.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                button.grid(row = grid[1], column = grid[0])
        elif grid is None:
            button.pack()

    def new_slider(self, scale, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        slider = ctk.CTkSlider(self.window)

        slider.configure(from_ = 0, 
                         to = scale, 
                         orientation= "horizontal", 
                         corner_radius = 5, 
                         fg_color = theme["text_colour"], 
                         width = helper.get_volume_slider_length(), 
                         button_hover_color = theme["highlight_colour"], 
                         button_color = theme["neutral_colour"], 
                         progress_color = theme["highlight_colour"],
                         command = lambda x: audioManager.set_mic_volume(slider.get()))

        if xyBuffer is not None:
            slider.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                slider.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                slider.grid(row = grid[1], column = grid[0])
        elif grid is None:
            slider.pack()

    def new_volume_bar(self, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        progress = ctk.CTkProgressBar(self.window, orientation= "horizontal")

        progress.configure(
                         corner_radius = 5, 
                         fg_color = theme["neutral_colour"], 
                         width = helper.get_volume_slider_length(), 
                         progress_color = theme["highlight_colour"])

        if xyBuffer is not None:
            progress.configure(padx = xyBuffer[0], pady = xyBuffer[1])

        if grid is not None:
            if sticky == "sticky":
                progress.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                progress.grid(row = grid[1], column = grid[0])
        elif grid is None:
            progress.pack()

        #sets the volume check which will display the volume of the user live
        def __user_volume_check__():
            level = audioManager.get_mic_volume()
            progress.set(level)
            self.window.after(20, __user_volume_check__)    
            print(level)

        __user_volume_check__()

    # ### debug ### #
    def frame_debug_colour(self):
        self.window.configure(bg = "green")