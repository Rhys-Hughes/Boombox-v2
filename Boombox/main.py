import tkinter as tk

import UIManager as UIM

if __name__ == "__main__":
    main_window = UIM.Window()

    main_window.initiate()

    main_window.format_window()
    
    main_window.new_title_label()

    main_window.close_loop()