#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import os
import sys

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== import custom font ======================================================================================================================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

font_path = "Quicksand-bold.ttf"
pyglet.font.add_file(resource_path(font_path))

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


    