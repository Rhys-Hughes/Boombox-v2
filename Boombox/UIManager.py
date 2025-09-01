import tkinter as tk
import ctypes
import customtkinter as ctk
import tkinter.font as tkFont

import helper, audioManager


title_font = ""
standard_font = ""
version_font = ""

class Window:
    def __init__(self):
        self.self = self
        self.window = None

    #---------------------------------------------------------------------------------- Frames / pages
    #create the window instance
    def initiate_page(self):
        self.window = ctk.CTk()
    
    #creates a new frame within the UI
    #
    # parent -> parent frame/page
    # grid -> tuple coordinades as (column, row)
    # sticky -> makes the frame fill the grid area it is in
    def initiate_frame(self, parent, grid = None, sticky = None):
        theme = helper.get_theme()
        self.window = ctk.CTkFrame(parent)

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
        
        self.window.configure(fg_color = theme["background_colour"])
    
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





    #---------------------------------------------------------------------------------- formatting
    #formats the page
    def format_page(self):
        #sets up the main window
        theme = helper.get_theme()
        dimensions = helper.get_dimensions()
    
        self.window.title("Boombox")
        self.window.geometry(dimensions)
        self.window.configure(fg_color = theme["background_colour"])
        self.window.iconbitmap(default=theme["logo"])

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(theme["logo"])

        ctk.set_appearance_mode("dark")

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





    #---------------------------------------------------------------------------------- widgets
    #adds a label to the page
    #
    # content -> string of Content
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    # sticky -> if "not sticky" the widget will not be sticky
    # xyBuffer -> touple which creates a buffer as (x, y)
    # style -> decides how the label will look
    def new_label(self, style, content = None, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        title_font = ctk.CTkFont(family = theme["title_font"][0], size = theme["title_font"][1])
        standard_font = ctk.CTkFont(family = theme["standard_font"][0], size = theme["standard_font"][1])
        version_font = ctk.CTkFont(family = theme["version_font"][0], size = theme["version_font"][1])

        label = ctk.CTkLabel(self.window, text = content)


        if style == "title":
            label.configure(fg_color= theme["background_colour"], 
                            text_color = theme["highlight_colour"],
                            corner_radius = 5,
                            font = title_font)
                        
        elif style == "version":
            label.configure(fg_color= theme["background_colour"], 
                            text_color = theme["text_colour"],
                            corner_radius = 5,
                            font = version_font,
                            text = helper.get_version())
            
        elif style == "neutral":
            label.configure(fg_color= theme["neutral_colour"], 
                            text_color = theme["background_colour"],
                            corner_radius = 5,
                            font = standard_font)
                    
        elif style == "standard":
            label.configure(fg_color= theme["background_colour"], 
                            text_color = theme["text_colour"],
                            corner_radius = 5,
                            font = standard_font)
                    

        #i am sure there is a cleaner way to do this but this can be improved later, it works currently

        if grid is not None:

            if sticky == "sticky":

                if xyBuffer is not None:
                    label.grid(row = grid[1], column = grid[0], sticky = "nsew", padx = xyBuffer[0], pady = xyBuffer[1])
                
                else:
                    label.grid(row = grid[1], column = grid[0])

            else:

                if xyBuffer is not None:
                    label.grid(row = grid[1], column = grid[0], padx = xyBuffer[0], pady = xyBuffer[1])
                
                else:
                    label.grid(row = grid[1], column = grid[0])

        elif grid is None:

            if xyBuffer is not None:
                label.pack(padx = xyBuffer[0], pady = xyBuffer[1])

            else:
                label.pack()

    def new_button(self, style, content, grid = None, command = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        title_font = ctk.CTkFont(family = theme["title_font"][0], size = theme["title_font"][1])
        standard_font = ctk.CTkFont(family = theme["standard_font"][0], size = theme["standard_font"][1])
        version_font = ctk.CTkFont(family = theme["version_font"][0], size = theme["version_font"][1])

        if command is None:
            button = ctk.CTkButton(self.window, text = content)
        else:
            button = ctk.CTkButton(self.window, text = content, command = command)

        if style == "neutral":
            button.configure(hover_color = theme["highlight_colour"], 
                            fg_color= theme["neutral_colour"], 
                            text_color = theme["background_colour"],
                            font=standard_font,
                            corner_radius = 5,
                            width = 50)
                    
        elif style == "standard":
            button.configure(hover_color = theme["neutral colour"],
                            fg_color= theme["background_colour"], 
                            text_color = theme["text_colour"],
                            font = standard_font,
                            corner_radius = 5,
                            width = 50)
        
        elif style == "highlight":
            button.configure(hover_color = theme["neutral_colour"],
                            fg_color= theme["highlight_colour"], 
                            text_color = theme["background_colour"],
                            font = standard_font,
                            corner_radius = 5,
                            width = 50)

        #i am sure there is a cleaner way to do this but this can be improved later, it works currently

        if grid is not None:

            if sticky == "sticky":

                if xyBuffer is not None:
                    button.grid(row = grid[1], column = grid[0], sticky = "nsew", padx = xyBuffer[0], pady = xyBuffer[1])
                
                else:
                    button.grid(row = grid[1], column = grid[0])

            else:

                if xyBuffer is not None:
                    button.grid(row = grid[1], column = grid[0], padx = xyBuffer[0], pady = xyBuffer[1])
                
                else:
                    button.grid(row = grid[1], column = grid[0])

        elif grid is None:

            if xyBuffer is not None:
                button.pack(padx = xyBuffer[0], pady = xyBuffer[1])

            else:
                button.pack()

    def new_slider(self, scale, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        slider = ctk.CTkSlider(self.window)

        slider.configure(from_ = 0, 
                         to = scale, 
                         orientation= "horizontal", 
                         fg_color = theme["text_colour"], 
                         width = helper.get_volume_slider_length(), 
                         button_hover_color = theme["neutral_colour"], 
                         button_color = theme["highlight_colour"], 
                         progress_color = theme["highlight_colour"],
                         height = 20,
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
        
        slider.set(1)

    def new_volume_bar(self, grid = None, sticky = None, xyBuffer = None):
        theme = helper.get_theme()

        progress = ctk.CTkProgressBar(self.window, orientation= "horizontal")

        progress.configure(corner_radius = 5, 
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
            level = audioManager.get_mic_level()
            progress.set(level / 100)

            #print("-" * round(int(level), 0))
            print(level)
            self.window.after(20, __user_volume_check__)    
            

        __user_volume_check__()



    #---------------------------------------------------------------------------------- debug
    # ### debug ### #
    def frame_debug_colour(self):
        self.window.configure(bg = "green")