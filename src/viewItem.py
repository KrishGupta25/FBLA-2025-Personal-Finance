#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import json
from geopy.geocoders import Nominatim
import googlemaps
from urllib.request import urlopen
#=========================== import all required functions ======================================================================================================================================================
from errorPage import error

#=========================== api setup ======================================================================================================================================================
apiKey = "AIzaSyAsIHQh_QzAprYbhOHPs5o5usSKSJSqvjU"
url1 = 'http://ipinfo.io/json'
response = urlopen(url1)
data = json.load(response)
home = data['loc']
loc = Nominatim(user_agent="Geopy Library")
gmaps = googlemaps.Client(key= apiKey)
#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== function for button highlighting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

check = 0

#=========================== function to create add item frame ======================================================================================================================================================
def viewItem(root, listbox):
#=========================== add organization frame ======================================================================================================================================================
    global check
    if check == 0:
        temp = listbox.selection()
        if len(temp) == 0:
            error("Please select an organization to edit", root)
        elif len(temp) > 1:
            error("You can only select one organization to edit at a time", root)
        else:
            check = 1

            selection = listbox.item(temp, option="values")
            destination = selection[2]

            viewItemFrame = ctk.CTkFrame(root, width=700, height=600, fg_color=color, border_color="#1e2121", border_width=4)
            viewItemFrame.place(relx=1, rely=0, anchor="ne")
            viewItemFrame.focus_set()

            def back():
                global check
                viewItemFrame.place_forget()
                check = 0

            backButton = ctk.CTkButton(viewItemFrame, text="x", font=font(20), command=back, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.04, rely=0.02, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)


#=========================== find distance and time ======================================================================================================================================================
            getLoc = loc.geocode("University of Florida, Gainesville, FL 32611")
            newHome = home.rsplit(",")
            print(newHome)
            print(getLoc.latitude)
            print(getLoc.longitude)

            origin_latitude = newHome[0]
            origin_longitude = newHome[1]
            destination_latitude = getLoc.latitude
            destination_longitude = getLoc.longitude
            distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)], mode='driving')['rows'][0]['elements'][0]

            print(distance)

        