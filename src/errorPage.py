#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import ctypes
import sys
from pathlib import Path

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== import custom font ======================================================================================================================================================
def fetch_resource(rsrc_path):
    """Loads resources from the temp dir used by pyinstaller executables"""
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        return rsrc_path  # not running as exe, just return the unaltered path
    else:
        return base_path.joinpath(rsrc_path)


def load_font(font_path, private=True, enumerable=False):
    """Add the font at 'font_path' as a Windows font resource"""
    FR_PRIVATE = 0x10
    FR_NOT_ENUM = 0x20
    flags = (FR_PRIVATE * int(private)) | (FR_NOT_ENUM * int(1 - enumerable))
    font_fetch = str(fetch_resource(font_path))
    path_buf = ctypes.create_unicode_buffer(font_fetch)
    add_font = ctypes.windll.gdi32.AddFontResource.ExW
    font_added = add_font(ctypes.byref(path_buf), flags, 0)
    return bool(font_added)  # True if the font was added successfully

font = "Quicksand"
#=========================== function to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand",size)

#=========================== function for error page ======================================================================================================================================================
def error(message, root):
    newError = ctk.CTkFrame(root, width = 1200, height = 600, fg_color= color)
    newError.place(relx = 0, rely = 0, anchor = "nw")

    label = ctk.CTkLabel(newError, text= message, font = font(30), fg_color = color)
    label.configure(anchor="center")
    label.place(relx= 0.5, rely= 0.4, anchor = "center")

    loginButton = ctk.CTkButton(newError, text="Ok", font=font(25), command= newError.place_forget, fg_color=accent, hover_color="#63C28D", text_color= color)
    loginButton.place(relx=0.5, rely=0.8, anchor="center")


    