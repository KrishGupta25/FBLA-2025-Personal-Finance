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
    #Create new sign up frame over login page
    infoFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    infoFrame.place(relx= 0, rely= 0)
    




