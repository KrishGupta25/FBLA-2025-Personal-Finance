#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import string

# Import all commands
from error import error

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
def info(root):

    #Create new info frame over "root" which in this case is "signupFrame"
    infoFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    infoFrame.place(relx= 0, rely= 0)

    nameText = ctk.CTkLabel(infoFrame, text="Name", font=font(15))
    nameText.place(relx=0.498, rely=0.05, anchor="center")

    nameEntry = ctk.CTkEntry(infoFrame, font = font(15), placeholder_text = "Name", width = 400, height= 40, justify = "center")
    nameEntry.place(relx= 0.5, rely= 0.125, anchor= "center")

    prefferedNameText = ctk.CTkLabel(infoFrame, text="Preffered Name", font=font(15))
    prefferedNameText.place(relx=0.5, rely=0.255, anchor="center")

    prefferedNameEntry = ctk.CTkEntry(infoFrame, font = font(15), placeholder_text = "Preffered Name", width = 400, height= 40, justify = "center")
    prefferedNameEntry.place(relx= 0.5, rely= 0.33, anchor= "center")


    def exit():

        #Checking password for at least one uppercase letter, one lowercase letter, one special character, and one number, and at least 8 characters
        #Checking password for "@" symbol 
        #Checking both for no spaces and making sure they arent blank
            name = nameEntry.get()
            prefferedName = prefferedNameEntry.get()
            temp = {"name": name, "preffered name": prefferedName}
            loginInfo.insert_one(temp)
            infoFrame.place_forget()
            print("hi")
            
    

    signUpButton = ctk.CTkButton(infoFrame, text="Sign Up", font=font(25), command= exit, fg_color= accent, hover_color="#63C28D", text_color=color )
    signUpButton.place(relx=0.5, rely=0.8, anchor="center")






    




