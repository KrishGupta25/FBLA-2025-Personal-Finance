#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import string

# Import all commands
from errorPage import error

#Creates connection to database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#Import custom font
pyglet.font.add_file('./assets/Quicksand-Bold.ttf')

#Function to simplify font size
def font(size):
    return ("Quicksand",size)

#Setting the default color
color = "#121414"
accent = "#3cb371"

def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

#Instantiatation of a new page for the signup
def info(root,email,password):

    #Create new info frame over "root" which in this case is "loginFrame"
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


    def exit():

        #Checking password for at least one uppercase letter, one lowercase letter, one special character, and one number, and at least 8 characters
        #Checking password for "@" symbol 
        #Checking both for no spaces and making sure they arent blank
            first = firstNameEntry.get()
            last = lastNameEntry.get()
            prefferedName = prefferedNameEntry.get()
            databaseInformation = {"email": email, "password": password, "firstName": first, "lastName": last, "prefferedName": prefferedName}
            loginInfo.insert_one(databaseInformation)
            infoFrame.place_forget()
            
    

    signUpButton = ctk.CTkButton(infoFrame, text="Sign Up", font=font(25), command= exit, fg_color= accent, hover_color="#63C28D", text_color=color )
    signUpButton.place(relx=0.5, rely=0.875, anchor="center")







    




