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
transactionInfo = db["transactionInfo"]

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


#=========================== function to create add item frame ======================================================================================================================================================
def filter(root, listbox):
#=========================== add organization frame ======================================================================================================================================================
    filterFrame = ctk.CTkFrame(root, width=1200, height=200, fg_color=color, border_color="#1e2121", border_width=4)
    filterFrame.place(relx=0, rely=0, anchor="nw")
    filterFrame.focus_set()

    backButton = ctk.CTkButton(filterFrame, text="x", font=font(20), command= filterFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
    backButton.place(relx=.04, rely=0.02, anchor="nw")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave)

    labelText = ctk.CTkLabel(filterFrame, text="Filter by resource", font=font(20), fg_color=color, text_color="white")
    labelText.place(relx=0.5, rely=0.1, anchor="center")

    internship = tk.StringVar()
    internshipCheckbox = ctk.CTkCheckBox(filterFrame, text="Internship", hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white", onvalue= "on", offvalue= "off", variable=internship)
    internshipCheckbox.place(relx=0.25, rely=0.25, anchor= "center")

    volunteer = tk.StringVar()
    volunteerCheckbox = ctk.CTkCheckBox(filterFrame, text="Volunteering", hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white", onvalue= "on", offvalue= "off", variable=volunteer)
    volunteerCheckbox.place(relx=0.75, rely=0.25, anchor= "center")

    fundraising = tk.StringVar()
    fundraisingCheckbox = ctk.CTkCheckBox(filterFrame, text="Fundraising", hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white", onvalue= "on", offvalue= "off", variable= fundraising)
    fundraisingCheckbox.place(relx=0.25, rely=0.75, anchor= "center")

    college = tk.StringVar()
    collegeCheckbox = ctk.CTkCheckBox(filterFrame, text="College help", hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white",variable=college, onvalue= "on", offvalue= "off")
    collegeCheckbox.place(relx=0.75, rely=0.75, anchor= "center")

    def submit():
        filtered = list()
        final = list()
        if internship.get() == "on":
            filtered.append("Internship")
        if volunteer.get() == "on":
            filtered.append("Volunteering")
        if fundraising.get() == "on":
            filtered.append("Fundraising")
        if college.get() == "on":
            filtered.append("College_help")

        if len(filtered) > 0 and len(filtered) != 4:
            orgs = transactionInfo.find()
            for org in orgs:
                for item in filtered:
                    if item == org["resources"]:
                        final.append(org)
            count = 0
            for item in listbox.get_children():
                listbox.delete(item)
            for item in final:
                listbox.insert(parent='', index='end', text= "", iid= count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
                count+= 1
        else:
            orgs = transactionInfo.find()
            count = 0
            for item in listbox.get_children():
                listbox.delete(item)
            for item in orgs:
                listbox.insert(parent='', index='end', text="", iid=count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
                count += 1

        filterFrame.place_forget()

    submitButton = ctk.CTkButton(filterFrame, text="Submit", font=font(18), command=submit, fg_color=color, hover_color=color, text_color="white")
    submitButton.place(relx=0.5, rely=0.375, anchor="center")
    submitButton.bind("<Enter>", on_enter)
    submitButton.bind("<Leave>", on_leave)

    def reset():
        orgs = transactionInfo.find()
        count = 0
        for item in listbox.get_children():
            listbox.delete(item)
        for item in orgs:
            listbox.insert(parent='', index='end', text="", iid=count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
            count += 1

        filterFrame.place_forget()

    resetButton = ctk.CTkButton(filterFrame, text="Reset", font=font(18), command= reset, fg_color=color, hover_color=color, text_color="white")
    resetButton.place(relx=0.5, rely=0.625, anchor="center")
    resetButton.bind("<Enter>", on_enter)
    resetButton.bind("<Leave>", on_leave)

