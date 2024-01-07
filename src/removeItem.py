#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error

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


#=========================== function to create edit item frame ======================================================================================================================================================
def removeItem(root, listbox):
    temp = listbox.selection()
    delete = list()
    if len(temp) == 0:
        error("Please select at least one Organization to delete", root)
    else:
        orgs = orgInfo.find()
        selection = list()
        for item in temp:
            selection.append(listbox.item(item, option="values"))
        for select in selection:
            for org in orgs:
                if select[0] == org["orgName"] and select[1] == org["resources"] and select[2] == org["location"] and select[3] == org["contactInfo"]:
                    delete.append({"orgName":select[0],"resources":select[1],"location":select[2],"contactInfo":select[3]})
                    
        for item in delete:
            orgInfo.delete_one(item)
            count = 0

        for item in listbox.get_children():
            listbox.delete(item)
        for item in orgs:
            listbox.insert(parent='', index='end', text= "", iid= count, values= (item["orgName"], item["location"], item["resources"], item["contactInfo"]) )
            count+= 1        