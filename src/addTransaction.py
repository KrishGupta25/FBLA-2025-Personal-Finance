#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import random as rand
from datetime import datetime

#=========================== import all required functions ======================================================================================================================================================
from errorPage import error
from success import success

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== function to simplify font size ======================================================================================================================================================
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

#=========================== global variable for transaction frame state ======================================================================================================================================================
check = 0

#=========================== function to create add transaction frame ======================================================================================================================================================
def addTransaction(root, listbox, tempLabel, user, switch, projectid):
    #=========================== define query for retrieving transaction data ======================================================================================================================================================
    query = {
        "$or": [
            { "_id": { "$type": "string", "$regex": str(user)+"projectNames"+ str(projectid)}},
            {
                "$expr": {
                    "$regexMatch": {
                        "input": { "$toString": "$_id" },
                        "regex": "^specificString"
                    }
                }
            }
        ]
    }

    transactionInfo = db[str(user)]
    global check
    if check == 0:
        check = 1
        addTransactionFrame = ctk.CTkFrame(root, width=500, height=600, fg_color=color, border_color="#1e2121", border_width=4)
        addTransactionFrame.place(relx=1, rely=0, anchor="ne")
        addTransactionFrame.focus_set()

        #=========================== function to close the transaction frame ======================================================================================================================================================
        def back():
            global check
            addTransactionFrame.place_forget()
            check = 0

        #=========================== back button setup ======================================================================================================================================================
        backButton = ctk.CTkButton(addTransactionFrame, text="x", font=font(20), command=back, fg_color=color, hover_color=color, width=0, height=0)
        backButton.place(relx=.04, rely=0.02, anchor="nw")
        backButton.bind("<Enter>", on_enter)
        backButton.bind("<Leave>", on_leave)

        #=========================== amount entry field ======================================================================================================================================================
        amountEntryText = ctk.CTkLabel(addTransactionFrame, text="Enter Amount", font=font(15), fg_color=color, text_color="white")
        amountEntryText.place(relx=0.12, rely=0.15, anchor="w")
        amountEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Amount", width=400, height=40, justify="center", fg_color=color, text_color="white")
        amountEntry.place(relx=0.5, rely=0.2, anchor="center")

        #=========================== category dropdown menu ======================================================================================================================================================
        categoryText = ctk.CTkLabel(addTransactionFrame, text="Category", font=font(15), fg_color=color, text_color="white")
        categoryText.place(relx=0.12, rely=0.35, anchor="w")
        categoryFrame = ctk.CTkFrame(
            addTransactionFrame,
            width=400,
            height=40,
            fg_color=color,
            border_color="#565B5E", 
            border_width=2,
        )
        categoryFrame.place(relx=0.5, rely=0.4, anchor="center")
        categories = ["Income", "Rent", "Groceries", "Utilities", "Transportation", "Entertainment", "Other"]
        categoryDropdown = ctk.CTkOptionMenu(
            categoryFrame,
            values=categories,
            font=font(15),
            fg_color=color,
            text_color="white",
            button_color=accent,
            button_hover_color="#1c5c3c",
        )
        categoryDropdown.place(relx=0.5, rely=0.5, anchor="center")
        categoryDropdown.set("Select a category")

        #=========================== date entry field ======================================================================================================================================================
        dateText = ctk.CTkLabel(addTransactionFrame, text="Date", font=font(15), fg_color=color, text_color="white")
        dateText.place(relx=0.12, rely=0.55, anchor="w")
        dateEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Enter a date", width=400, height=40, justify="center", fg_color=color, text_color="white", state="normal")
        dateEntry.place(relx=0.5, rely=0.6, anchor="center")

        #=========================== optional information field ======================================================================================================================================================
        optionalInfoText = ctk.CTkLabel(addTransactionFrame, text="Enter Any Extra Information", font=font(15), fg_color=color, text_color="white")
        optionalInfoText.place(relx=0.12, rely=0.75, anchor="w")
        optionalInfoEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Optional Info", width=400, height=40, justify="center", fg_color=color, text_color="white")
        optionalInfoEntry.place(relx=0.5, rely=0.8, anchor="center")

        #=========================== submit function to validate and insert transaction ======================================================================================================================================================
        def submit():
            global check
            # Validation logic
            if switch == 0:
                orgs = transactionInfo.find()
            else:
                orgs = transactionInfo.find(query)
            ...
            success("Transaction Was Successfully Added To The Database!", root)

        #=========================== submit button setup ======================================================================================================================================================
        submitButton = ctk.CTkButton(addTransactionFrame, text="Submit", font=font(18), command=submit, fg_color=color, hover_color=color, text_color="white")
        submitButton.place(relx=0.5, rely=0.9, anchor="center")
        submitButton.bind("<Enter>", on_enter)
        submitButton.bind("<Leave>", on_leave)
    else:
        error("Please Close The Existing 'Add Organization' Page First", root)
