#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#=========================== set default colors ======================================================================================================================================================
color = "#121414"

#=========================== import custom font ======================================================================================================================================================
pyglet.font.add_file('./assets/Quicksand-Bold.ttf')

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


    okButton= ctk.CTkButton(newError, text= "Ok", font= font(25), fg_color= color, command= newError.place_forget)
    okButton.place(relx= 0.5, rely= 0.8, anchor= "center")


    