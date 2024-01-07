#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import time


#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from addItem import addItem
from editItem import editItem
from removeItem import removeItem

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== import custom font ======================================================================================================================================================
pyglet.font.add_file('Quicksand-Bold.ttf')

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

#=========================== creates new page for search ======================================================================================================================================================
def searchPage(root):
    orgs = orgInfo.find()

    searchFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    searchFrame.place(relx= 0, rely= 0, anchor= "nw")

    searchLabel = ctk.CTkLabel(searchFrame, text= "🔎", font=font(20))
    searchLabel.place(relx=0.31, rely=0.075, anchor="center")
    
    searchEntry = ctk.CTkEntry(searchFrame, font= font(15), width= 400, height= 20, justify= "left", placeholder_text="search by name")
    searchEntry.place(relx= 0.5, rely= 0.075, anchor= "center")
    searchEntry.focus_force()

    backButton = ctk.CTkButton(searchFrame, text="⌂", font=font(40), command= searchFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
    backButton.place(relx=.04, rely=0.02, anchor="nw")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave)


    #=========================== listbox style ======================================================================================================================================================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= color, background = color, foreground= "white", font= ("Quicksand", 12), rowheight= 100, highlightbackground = color, highlightcolor= accent)
    style.configure("Treeview.Heading", background = color, foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    style.map('Treeview', background=[('selected', '#292929')])

#=========================== create listbox ======================================================================================================================================================
    listbox = ttk.Treeview(searchFrame, selectmode="extended",columns=("c1", "c2", "c3", "c4"),show="headings", height= 6)
    listbox.column("# 1", anchor="center", width = 365)
    listbox.heading("# 1", text="Name")
    listbox.column("# 2", anchor="center", width = 365)
    listbox.heading("# 2", text="Resources")
    listbox.column("# 3", anchor="center", width = 365)
    listbox.heading("# 3", text="Location")
    listbox.column("# 4", anchor="center", width = 365)
    listbox.heading("# 4", text="Contact")

    listbox.place(relx=.5, rely=.55, anchor="center")

    count = 0
    for item in listbox.get_children():
        listbox.delete(item)
    for item in orgs:
        listbox.insert(parent='', index='end', text= "", iid= count, values= (item["orgName"], item["location"], item["resources"], item["contactInfo"]) )
        count+= 1

    def on_key_press():
        search= searchEntry.get()
        search = list(search)
        print(search)

    
    searchEntry.bind("<Key>", lambda x: on_key_press())

