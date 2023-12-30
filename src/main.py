#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#Import all commands
from signUp import signUp

#Set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["FBLAMain"]
loginInfo = db["login_info"]


#set default color
color = "#1e1e1e"
#Import custom font
pyglet.font.add_file('assets/circular-std-medium-500.ttf')

#Function to simplify font size
def font(size):
    return ("circular",size)


#Setting up the GUI
#Creates main home gui
root = ctk.CTk(fg_color = color) 
root.geometry("1200x600+180+120")
loginFrame = ctk.CTkFrame(root, width = 1200, height = 600, fg_color = color)
loginFrame.place(relx = 0, rely = 0)


#Creates login to xxxx label
loginLabel = ctk.CTkLabel(loginFrame, text="Login to xxxx", font=font(50))
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

usernameLabel = ctk.CTkLabel(loginFrame, text="Email", font=font(15))
usernameLabel.place(relx=0.335, rely=0.36, anchor="nw")
usernameEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center", show= "*")
usernameEntry.place(relx= 0.5, rely= 0.45, anchor= "center")

passLabel = ctk.CTkLabel(loginFrame, text="Password", font=font(15))
passLabel.place(relx=0.335, rely=0.51, anchor="nw")
passEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
passEntry.place(relx= 0.5, rely= 0.6, anchor= "center")


def login():
    logins = list()
    logins = loginInfo.find()
    for items in logins:
        if usernameEntry.get() == items['email'] and passEntry.get() == items['password']:
            print("hello")


#Creates log in up button
loginButton = ctk.CTkButton(loginFrame, text="Login in to xxxx", font=font(25), command= login, fg_color=color)
loginButton.place(relx=0.5, rely=0.75, anchor="center")

#Creates sign up button
signupButton = ctk.CTkButton(loginFrame, text="Sign up for xxxx", font=font(25), command= lambda:(signUp(loginFrame)), fg_color=color)
signupButton.place(relx=0.5, rely=0.9, anchor="center")







#Keeps gui running
if __name__ == "__main__":
    root.mainloop()



