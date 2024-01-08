# =========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

# =========================== import all required functions ======================================================================================================================================================

from errorPage import error
from pickingOrganization import pickingOrg

# =========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

# =========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

# =========================== function to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

# =========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

# =========================== function for button highlighting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

# =========================== creates a new page for personal info ======================================================================================================================================================
def info(root, email, password, delete):
    infoFrame = ctk.CTkFrame(root, width=1200, height=600, fg_color=color)
    infoFrame.place(relx=0, rely=0)

    labelText = ctk.CTkLabel(infoFrame, text="Personal Info", font=font(30), fg_color=color, text_color="white")
    labelText.place(relx=0.5, rely=0.05, anchor="center")

    firstNameText = ctk.CTkLabel(infoFrame, text="First Name", font=font(15), fg_color=color, text_color="white")
    firstNameText.place(relx=0.34, rely=0.275, anchor="w")

    firstNameEntry = ctk.CTkEntry(infoFrame, font=font(15), placeholder_text="First name", width=400, height=40, justify="center")
    firstNameEntry.place(relx=0.5, rely=0.325, anchor="center")

    lastNameText = ctk.CTkLabel(infoFrame, text="Last Name", font=font(15), fg_color=color, text_color="white")
    lastNameText.place(relx=0.34, rely=0.475, anchor="w")

    lastNameEntry = ctk.CTkEntry(infoFrame, font=font(15), placeholder_text="Last name", width=400, height=40, justify="center")
    lastNameEntry.place(relx=0.5, rely=0.525, anchor="center")

    preferredNameText = ctk.CTkLabel(infoFrame, text="Preferred Name", font=font(15), fg_color=color, text_color="white")
    preferredNameText.place(relx=0.34, rely=0.675, anchor="w")

    preferredNameEntry = ctk.CTkEntry(infoFrame, font=font(15), placeholder_text="Preferred Name", width=400, height=40, justify="center")
    preferredNameEntry.place(relx=0.5, rely=0.725, anchor="center")

    backButton = ctk.CTkButton(infoFrame, text="⌂", font=font(40), command=lambda: [infoFrame.place_forget(), delete.place_forget()],fg_color=color, text_color="white", width=0, height=0)
    backButton.place(relx=.02, rely=0.001, anchor="nw")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave)

    # =========================== function to insert data input from the user into the database ======================================================================================================================================================
    def exit():
        first = firstNameEntry.get()
        last = lastNameEntry.get()
        preferredName = preferredNameEntry.get()
        first = first.capitalize()
        last = last.capitalize()
        preferredName = preferredName.capitalize()
        if first == "" or last == "" or preferredName == "":
            error("one or more of the required fields are empty", infoFrame)
        else:
            databaseInformation = {"email": email, "password": password, "firstName": first, "lastName": last,"preferredName": preferredName}
            loginInfo.insert_one(databaseInformation)
            infoFrame.place_forget()
            delete.place_forget()

    # =========================== create sign-up button ======================================================================================================================================================
    signUpButton = ctk.CTkButton(infoFrame, text="Sign Up", font=font(25), command=exit, fg_color=accent, text_color=color)
    signUpButton.place(relx=0.5, rely=0.875, anchor="center")