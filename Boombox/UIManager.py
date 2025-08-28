import tkinter as tk
import ctypes
import customtkinter as ctk

import helper

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

        #creates the basic window
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
        

    #adds a title to the page
    #
    # content -> string of Content
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    def new_title_label(self, content, grid = None, sticky = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["highlight_colour"], 
                        font=theme["title_font"])
        
        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label
    
    #displays the version of the software
    #
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    def new_version_label(self, grid = None, sticky = None):
        theme = helper.get_theme()
        version = helper.get_version()

        label = tk.Label(self.window, text = version)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["text_colour"], 
                        font=theme["version_font"])
        
        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    #adds a title to the page
    #
    # content -> string of Content
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    def new_label(self, content, grid = None, sticky = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["background_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["text_colour"], 
                        font=theme["standard_font"])
        
        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    #adds a title to the page
    #
    # content -> string of Content
    # grid -> tuple coordinades as (column, row)  {if left blank, will pack the label}
    def new_neutral_label(self, content, grid = None, sticky = None):
        theme = helper.get_theme()

        label = tk.Label(self.window, text = content)
        label.configure(activebackground = theme["highlight_colour"], 
                        bg= theme["neutral_colour"], 
                        bd = theme["border_width"], 
                        fg = theme["background_colour"], 
                        font=theme["standard_font"])
        
        if grid is not None:
            if sticky == "sticky":
                label.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                label.grid(row = grid[1], column = grid[0])
        elif grid is None:
            label.pack()

        return label

    def new_button(self, content, grid = None, command = None, sticky = None):
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

        if grid is not None:
            if sticky == "sticky":
                button.grid(row = grid[1], column = grid[0], sticky = "nsew")
            else:
                button.grid(row = grid[1], column = grid[0])
        elif grid is None:
            button.pack()




    

    # ### debug ### #
    def frame_debug_colour(self):
        self.window.configure(bg = "green")