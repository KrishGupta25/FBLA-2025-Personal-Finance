#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import ctypes
import sys
from pathlib import Path
#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from pickingOrganization import pickingOrg

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

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

#=========================== creates new page for personal info ======================================================================================================================================================
def info(root,email,password, delete):

    infoFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    infoFrame.place(relx= 0, rely= 0)

    labelText = ctk.CTkLabel(infoFrame, text="Personal Info", font=font(30))
    labelText.place(relx=0.5, rely=0.15, anchor="center")

    firstNameText = ctk.CTkLabel(infoFrame, text="First Name", font=font(15))
    firstNameText.place(relx=0.34, rely=0.275, anchor="w")

    firstNameEntry = ctk.CTkEntry(infoFrame, font = font(15), placeholder_text = "First name", width = 400, height= 40, justify = "center")
    firstNameEntry.place(relx= 0.5, rely= 0.325, anchor= "center")

    lastNameText = ctk.CTkLabel(infoFrame, text="Last Name", font=font(15))
    lastNameText.place(relx=0.34, rely=0.475, anchor="w")

    lastNameEntry = ctk.CTkEntry(infoFrame, font = font(15), placeholder_text = "Last name", width = 400, height= 40, justify = "center")
    lastNameEntry.place(relx= 0.5, rely= 0.525, anchor= "center")

    prefferedNameText = ctk.CTkLabel(infoFrame, text="Preffered Name", font=font(15))
    prefferedNameText.place(relx=0.34, rely=0.675, anchor="w")

    prefferedNameEntry = ctk.CTkEntry(infoFrame, font = font(15), placeholder_text = "Preffered Name", width = 400, height= 40, justify = "center")
    prefferedNameEntry.place(relx= 0.5, rely= 0.725, anchor= "center")

    backButton = ctk.CTkButton(infoFrame, text="⌂", font=font(40), command= lambda: [infoFrame.place_forget(), delete.place_forget()], fg_color=color, hover_color=color, width=0, height=0)
    backButton.place(relx=.02, rely=0.001, anchor="nw")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave)


#=========================== function to insert data input form the user into the database ======================================================================================================================================================
    def exit():
            first = firstNameEntry.get()
            last = lastNameEntry.get()
            prefferedName = prefferedNameEntry.get()
            first = first.capitalize()
            last = last.capitalize()
            prefferedName = prefferedName.capitalize()
            if first == "" or last == "" or prefferedName == "":
                error("one or more of the required fields are empty", infoFrame)
            else:
                databaseInformation = {"email": email, "password": password, "firstName": first, "lastName": last, "prefferedName": prefferedName}
                loginInfo.insert_one(databaseInformation)
                infoFrame.place_forget()
                delete.place_forget()
            
    
#=========================== create sign up button ======================================================================================================================================================
    signUpButton = ctk.CTkButton(infoFrame, text="Sign Up", font=font(25), command= exit, fg_color= accent, hover_color="#63C28D", text_color=color )
    signUpButton.place(relx=0.5, rely=0.875, anchor="center")







    




