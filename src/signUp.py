#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

# Import all commands
from error import error

#Creates connection to database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#Import custom font
pyglet.font.add_file('assets/circular-std-medium-500.ttf')

#Function to simplify font size
def font(size):
    return ("circular",size)

#set default color
color = "#1e1e1e"

def signUp(root):
    #Create new sign up frame over login page
    newFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    newFrame.place(relx= 0, rely= 0)

    #Creates signup to xxxx label
    loginLabel = ctk.CTkLabel(newFrame, text="Sign up for xxxx", font=font(50))
    loginLabel.place(relx=0.5, rely=0.2, anchor="center")

    emailLabel = ctk.CTkLabel(newFrame, text="Email", font=font(15))
    emailLabel.place(relx=0.335, rely=0.41, anchor="nw")
    emailEntry = ctk.CTkEntry(newFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center")
    emailEntry.place(relx= 0.5, rely= 0.5, anchor= "center")

    passLabel = ctk.CTkLabel(newFrame, text="Password", font=font(15))
    passLabel.place(relx=0.335, rely=0.61, anchor="nw")
    passEntry = ctk.CTkEntry(newFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
    passEntry.place(relx= 0.5, rely= 0.7, anchor= "center")

    def enter():
        email= emailEntry.get()
        password = passEntry.get()
        if email.find(" ") != -1 or password.find(" ") != -1 or email == "" or password == "":
            error("one or more of the required fields are empty/entries cannot contain spaces", newFrame)
        else:
            temp = {"email": email, "password": password}
            loginInfo.insert_one(temp)
            newFrame.place_forget()

        
    enterButton = ctk.CTkButton(newFrame, text="Sign up", font=font(25), command= enter, fg_color= color)
    enterButton.place(relx=0.5, rely=0.85, anchor="center")

    
