#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import ctypes
import sys
from pathlib import Path
#=========================== import all required functions ======================================================================================================================================================

from errorPage import error

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== import custom font ======================================================================================================================================================
def fetch_resource(rsrc_path):
    """Loads resources from the temp dir used by pyinstaller executables"""
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        return rsrc_path  # not running as exe, just return the unaltered path
    else:
        return base_path.joinpath(rsrc_path)


def load_font(font_path, private=True, enumerable=False):
    """Add the font at 'font_path' as a Windows font resource"""
    FR_PRIVATE = 0x10
    FR_NOT_ENUM = 0x20
    flags = (FR_PRIVATE * int(private)) | (FR_NOT_ENUM * int(1 - enumerable))
    font_fetch = str(fetch_resource(font_path))
    path_buf = ctypes.create_unicode_buffer(font_fetch)
    add_font = ctypes.windll.gdi32.AddFontResource.ExW
    font_added = add_font(ctypes.byref(path_buf), flags, 0)
    return bool(font_added)  # True if the font was added successfully

font = "Quicksand"

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