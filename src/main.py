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


#Creates login to xxxx label
loginLabel = ctk.CTkLabel(root, text="Login to xxxx", font=font(50))
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#Creates sign up button
signupButton = ctk.CTkButton(root, text="Sign up for xxxx", font=font(25), command= lambda:(signUp(root)))
signupButton.place(relx=0.5, rely=0.8, anchor="center")




#Keeps gui running
if __name__ == "__main__":
    root.mainloop()



