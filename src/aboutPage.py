#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#Import all commands
from errorPage import error
from signUp import signUp
from pickingOrganization import pickingOrg 

#Set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#set default color
color = "#121414"
accent = "#3cb371"

#Import custom font
pyglet.font.add_file('./assets/Quicksand-Bold.ttf')

#Function to simplify font size
def font(size):
    return ("Quicksand",size)

def about(root, forget):
    forget.place_forget()
    aboutFrame = ctk.CTkFrame(root, width=1200, height=600, bg_color= color)
    aboutFrame.place(relx= 0, rely= 0, anchor= "nw")