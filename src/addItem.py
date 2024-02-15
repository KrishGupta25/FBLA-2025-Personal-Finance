#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from success import success

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== function for button highlighting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

check = 0

#=========================== function to create add item frame ======================================================================================================================================================
def addItem(root, listbox):
#=========================== add organization frame ======================================================================================================================================================
    global check
    if check == 0:
        check = 1
        addItemFrame = ctk.CTkFrame(root, width=500, height=600, fg_color=color, border_color="#1e2121", border_width=4)
        addItemFrame.place(relx=1, rely=0, anchor="ne")
        addItemFrame.focus_set()

        def back():
            global check
            addItemFrame.place_forget()
            check = 0

        backButton = ctk.CTkButton(addItemFrame, text="x", font=font(20), command=back, fg_color=color, hover_color=color, width=0, height=0)
        backButton.place(relx=.04, rely=0.02, anchor="nw")
        backButton.bind("<Enter>", on_enter)
        backButton.bind("<Leave>", on_leave)

        labelText = ctk.CTkLabel(addItemFrame, text="Add Organization", font=font(20), fg_color=color, text_color="white")
        labelText.place(relx=0.5, rely=0.05, anchor="center")

        orgNameText = ctk.CTkLabel(addItemFrame, text="Organization Name", font=font(15), fg_color=color, text_color="white")
        orgNameText.place(relx=0.12, rely=0.15, anchor="w")

        orgNameEntry = ctk.CTkEntry(addItemFrame, font=font(15), placeholder_text="Organization name", width=400, height=40, justify="center", fg_color=color, text_color="white")
        orgNameEntry.place(relx=0.5, rely=0.2, anchor="center")

        resourceText = ctk.CTkLabel(addItemFrame, text="Resources Available", font=font(15), fg_color=color, text_color="white")
        resourceText.place(relx=0.12, rely=0.35, anchor="w")

        resourceEntry = ctk.CTkEntry(addItemFrame, font=font(15), placeholder_text="Resources Available", width=400, height=40, justify="center", fg_color=color, text_color="white")
        resourceEntry.place(relx=0.5, rely=0.4, anchor="center")

        locationText = ctk.CTkLabel(addItemFrame, text="Location", font=font(15), fg_color=color, text_color="white")
        locationText.place(relx=0.12, rely=0.55, anchor="w")

        locationEntry = ctk.CTkEntry(addItemFrame, font=font(15), placeholder_text="Address", width=400, height=40, justify="center", fg_color=color, text_color="white")
        locationEntry.place(relx=0.5, rely=0.6, anchor="center")

        contactText = ctk.CTkLabel(addItemFrame, text="Direct Contact", font=font(15), fg_color=color, text_color="white")
        contactText.place(relx=0.12, rely=0.75, anchor="w")

        contactEntry = ctk.CTkEntry(addItemFrame, font=font(15), placeholder_text="Contact Info", width=400, height=40, justify="center", fg_color=color, text_color="white")
        contactEntry.place(relx=0.5, rely=0.8, anchor="center")

        def submit():
            global check
            orgs = orgInfo.find()
            if orgNameEntry.get() == "" or locationEntry.get() == "" or resourceEntry.get() == "" or contactEntry.get() == "":
                error("One or more fields are empty, please use N/A in replacement of an empty entry", root)
            else:
                check = 0
                orgInfo.insert_one({"orgName": orgNameEntry.get(), "resources": resourceEntry.get(), "location": locationEntry.get(), "contactInfo": contactEntry.get()})
                addItemFrame.place_forget()
                count = 0
                for item in listbox.get_children():
                    listbox.delete(item)
                for item in orgs:
                    listbox.insert(parent='', index='end', text="", iid=count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
                    count += 1
                success("org was succesfully added to the database", root)

        submitButton = ctk.CTkButton(addItemFrame, text="Submit", font=font(18), command=submit, fg_color=color, hover_color=color, text_color="white")
        submitButton.place(relx=0.5, rely=0.9, anchor="center")
        submitButton.bind("<Enter>", on_enter)
        submitButton.bind("<Leave>", on_leave)
    else:
        error("please close the existing 'add organization' page first", root)


