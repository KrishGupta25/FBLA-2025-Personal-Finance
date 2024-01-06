#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import string

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== import custom font ======================================================================================================================================================
pyglet.font.add_file('Quicksand-Bold.ttf')

#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand",size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== cunction for button highliting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'


#=========================== function to create add item frame ======================================================================================================================================================
def addItem(root):
#=========================== add organization frame ======================================================================================================================================================
    addItemFrame = ctk.CTkFrame(root, width= 500, height= 600, fg_color= color, border_color= "#1e2121", border_width=4)
    addItemFrame.place(relx= 1, rely= 0, anchor= "ne")

    backButton = ctk.CTkButton(addItemFrame, text="x", font=font(20), command= addItemFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
    backButton.place(relx=.04, rely=0.02, anchor="nw")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave)

    labelText = ctk.CTkLabel(addItemFrame, text="Add Organization", font=font(20))
    labelText.place(relx=0.5, rely=0.05, anchor="center")

    orgNameText = ctk.CTkLabel(addItemFrame, text="Organization Name", font=font(15))
    orgNameText.place(relx=0.12, rely=0.275, anchor="w")

    orgNameEntry = ctk.CTkEntry(addItemFrame, font = font(15), placeholder_text = "Organization name", width = 400, height= 40, justify = "center")
    orgNameEntry.place(relx= 0.5, rely= 0.325, anchor= "center")

    loacationText = ctk.CTkLabel(addItemFrame, text="Location", font=font(15))
    loacationText.place(relx=0.12, rely=0.475, anchor="w")

    loacationEntry = ctk.CTkEntry(addItemFrame, font = font(15), placeholder_text = "Address", width = 400, height= 40, justify = "center")
    loacationEntry.place(relx= 0.5, rely= 0.525, anchor= "center")

    resourceText = ctk.CTkLabel(addItemFrame, text="Resouces Avaliable", font=font(15))
    resourceText.place(relx=0.12, rely=0.675, anchor="w")

    resourceEntry = ctk.CTkEntry(addItemFrame, font = font(15), placeholder_text = "Resources Avaliable", width = 400, height= 40, justify = "center")
    resourceEntry.place(relx= 0.5, rely= 0.725, anchor= "center")

    def submit():
        if  orgNameEntry.get() == "" or loacationEntry.get() == "" or resourceEntry.get() == "":
            error("One or more fields are empty, please use N/A in replacement of an empty entry", root)
        else:
            orgInfo.insert_one({"orgName": orgNameEntry.get(), "location": loacationEntry.get(), "resources": resourceEntry.get()})
            addItemFrame.place_forget()


    submitButton = ctk.CTkButton(addItemFrame, text="Submit", font=font(18), command = submit, fg_color=color, hover_color=color)
    submitButton.place(relx=0.5, rely=0.85, anchor="center")
    submitButton.bind("<Enter>", on_enter)
    submitButton.bind("<Leave>", on_leave)
