#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import json
from geopy.geocoders import Nominatim
import googlemaps
from urllib.request import urlopen
import tkintermapview as tkm
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
            error("Please select an organization to view", root)
        elif len(temp) > 1:
            error("You can only select one organization to view at a time", root)
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
            backButton.place(relx=.04, rely=0.01, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)


#=========================== find distance and time ======================================================================================================================================================
            getLoc = gmaps.geocode(destination)
            newHome = home.rsplit(",")

            try:
                destination_latitude = getLoc[0]["geometry"]["location"]["lat"]
            except IndexError:
                error("Location either does not exist or is N/A", root)
                viewItemFrame.place_forget()
                check = 0

            origin_latitude = newHome[0]
            origin_longitude = newHome[1]
            destination_latitude = getLoc[0]["geometry"]["location"]["lat"]
            destination_longitude = getLoc[0]["geometry"]["location"]["lng"]
            distData = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)], mode='driving')['rows'][0]['elements'][0]

            print(distData)
            distance = distData['distance']['text'].split("k")
            time = distData['duration']['text']
            km = distance[0].replace(",", "")
            print(km)
            

            mapWidget = tkm.TkinterMapView(viewItemFrame, width= 840, height= 450)
            mapWidget.place(relx= .5, rely= .075, anchor="n")

            mapWidget.set_position((float(newHome[0])+float(destination_latitude))/2, (float(newHome[1])+float(destination_longitude))/2, marker=False)
            mapWidget.set_zoom(7)

            marker1 = mapWidget.set_marker(float(newHome[0]), float(newHome[1]), text="home")
            marker2= mapWidget.set_marker(float(destination_latitude), float(destination_longitude), text="destination")

            nameLabel = ctk.CTkLabel(viewItemFrame, text= selection[0], font=font(15), fg_color=color, text_color="white")
            nameLabel.place(relx=0.5, rely=0.68, anchor="n")

            distanceLabel = ctk.CTkLabel(viewItemFrame, text=f'Distance to location: {round(float(km)*0.621371,2)} miles', font=font(15), fg_color=color, text_color="white")
            distanceLabel.place(relx=0.02, rely=0.8, anchor="w")
            
            timeLabel = ctk.CTkLabel(viewItemFrame, text=f'Travel time to location: {time}', font=font(15), fg_color=color, text_color="white")
            timeLabel.place(relx=0.02, rely=0.9, anchor="w")

        