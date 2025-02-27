#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
from PIL import ImageTk, Image
import os
import sys

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from addTransaction import addTransaction
from editTransaction import editItem
from removeItem import removeItem
#from filter import filter
from report import report
from success import success

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]


#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
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

#=========================== funtion to create home page ======================================================================================================================================================
def detailedProject(root, email, id):

#=========================== find users preferred name and transaction details =================================================================================================================================
    temp = loginInfo.find({"email": email})
    for item in temp:
        user = item["preferredName"]
        pickingTransactionId = item["_id"]
    
    transactionInfo = db[str(pickingTransactionId)+"collection"]
    projectnames = db[str(pickingTransactionId)+"projectNames"]

    # Define the query
    query = {
        "$or": [
            # Condition for string _id
            { "_id": { "$type": "string", "$regex": str(pickingTransactionId)+"collectionprojectNames"+ str(id)}},
            # Condition for ObjectId _id
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

    # Execute the query
    print(str(pickingTransactionId)+"collectionprojectNames"+ str(id))
    transactions = transactionInfo.find(query)


#=========================== home page frame ======================================================================================================================================================
    detailedProjectFrame = ctk.CTkFrame(root, fg_color= color)
    detailedProjectFrame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1, anchor= "nw")

#=========================== listbox style ======================================================================================================================================================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= color, background = color, foreground= "white", font= ("Quicksand", 12), rowheight= 100, highlightbackground = color, highlightcolor= accent)
    style.configure("Treeview.Heading", background = color, foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    style.map('Treeview', background=[('selected', '#292929')])

#=========================== create listbox ======================================================================================================================================================
    listbox = ttk.Treeview(detailedProjectFrame, selectmode="extended",columns=("c1", "c2", "c3", "c4"),show="headings")
    listbox.column("# 1", anchor="center")
    listbox.heading("# 1", text="Amount")
    listbox.column("# 2", anchor="center")
    listbox.heading("# 2", text="Type")
    listbox.column("# 3", anchor="center")
    listbox.heading("# 3", text="Date")
    listbox.column("# 4", anchor="center")
    listbox.heading("# 4", text="Additional Info")

    listbox.place(relx=.5, rely=.5, relwidth= .9, relheight= .715, anchor="center")

#=========================== add/edit/remove/view transactionanization buttons ======================================================================================================================================================
    addtransactionButton = ctk.CTkButton(detailedProjectFrame, text="Add transaction", font=font(18), command = lambda:[addTransaction(detailedProjectFrame, listbox, totalLabel, str(pickingTransactionId)+"collection", 1, id)], fg_color=color, hover_color=color)
    addtransactionButton.place(relx=0.3, rely=0.91, anchor="center")
    addtransactionButton.bind("<Enter>", on_enter)
    addtransactionButton.bind("<Leave>", on_leave)
    #test

    edittransactionButton = ctk.CTkButton(detailedProjectFrame, text="Edit transaction", font=font(18), command = lambda:[editItem(detailedProjectFrame, listbox, totalLabel, str(pickingTransactionId)+"collection", 1, id)], fg_color=color, hover_color=color)
    edittransactionButton.place(relx=0.55, rely=0.91, anchor="center")
    edittransactionButton.bind("<Enter>", on_enter)
    edittransactionButton.bind("<Leave>", on_leave)

    removetransactionButton = ctk.CTkButton(detailedProjectFrame, text="Remove transaction", font=font(18), command = lambda:[removeItem(detailedProjectFrame, listbox, totalLabel, str(pickingTransactionId)+"collection", 1 , id)], fg_color=color, hover_color=color)
    removetransactionButton.place(relx=0.8, rely=0.91, anchor="center")
    removetransactionButton.bind("<Enter>", on_enter)
    removetransactionButton.bind("<Leave>", on_leave)

#=========================== insert listbox details ======================================================================================================================================================

    count = 0
    transactions = transactionInfo.find(query)
    for item in listbox.get_children():
        listbox.delete(item)
    for item in transactions:
        listbox.insert(parent='', index='end', text= "", iid= count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
        count+= 1

    searchLabel = ctk.CTkLabel(detailedProjectFrame, text= "🔎", font=font(20), fg_color=color, text_color="white")
    searchLabel.place(relx=0.49, rely=0.075, anchor="center")

    searchEntry = ctk.CTkEntry(detailedProjectFrame, font= font(15), justify= "left", placeholder_text="Search by type", fg_color=color, text_color="white")
    searchEntry.place(relx= 0.7, rely= 0.075,  relwidth= 8/21, relheight= 4/105,anchor= "center")
    final = list()

    def on_key_press(event):
        check = 0
        transactions = transactionInfo.find(query)
        search= searchEntry.get()
        if len(list(search)) > 0:
            final.clear()
            for item in transactions:
                name = item["resources"]
                newName = name[:len(list(search))]
                if len(list(search)) <= len(list(name)):
                    # not case sensitive search
                    if search == newName or search.capitalize() == newName:
                        final.append(item)

                count = 0
                for item in listbox.get_children():
                    listbox.delete(item)
                for item in final:
                    listbox.insert(parent='', index='end', text= "", iid= count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
                    count+= 1
        else:
            transactions = transactionInfo.find(query)
            count = 0
            for item in listbox.get_children():
                listbox.delete(item)
            for item in transactions:
                listbox.insert(parent='', index='end', text= "", iid= count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
                count+= 1

    
    searchEntry.bind("<KeyRelease>", on_key_press)
    

    transactions = transactionInfo.find(query)
    total = 0
    for transaction in transactions:
        if transaction["resources"] == "Income":
            total += round(transaction["amount"],2)
            total = round(total,2)
        else:
            total -= round(transaction["amount"],2)
            total = round(total,2)
        
        

    totalLabel = ctk.CTkLabel(detailedProjectFrame, text= "Total: " + str(total), font=font(18), fg_color=color, text_color="white")
    totalLabel.place(relx=0.02, rely=0.91, anchor="w")

    temp = projectnames.find()
    for item in temp:
        if int(item["_id"]) == int(id):
            name = item["projectName"]

    def changeName():
        changeNameFrame = ctk.CTkFrame(root, fg_color= "#0f1010")
        changeNameFrame.place(relx= .03, rely= .14, relwidth= 8/21, relheight= 4/21, anchor= "nw")

        changeNameLabel = ctk.CTkLabel(changeNameFrame, text= "Enter new project name:", font=font(15), fg_color=color, text_color="white")
        changeNameLabel.place(relx=0.14, rely=0.16, anchor="nw")

        changeNameEntry = ctk.CTkEntry(changeNameFrame, font=font(15), justify="center", fg_color=color, text_color="white")
        changeNameEntry.place(relx=0.5, rely=0.55, relwidth= 3/4, relheight= 1/5, anchor="center")
        changeNameEntry.insert(0, name)
        changeNameEntry.bind('<FocusIn>', lambda x: changeNameEntry.select_range(0, "end"))

        def submit():
            projectnames.replace_one({"_id": int(id)}, {"_id": int(id), "projectName": changeNameEntry.get()})
            changeNameFrame.place_forget()
            success("Project name changed", root)
            labelText.configure(text="Project name: " + changeNameEntry.get())

        submitButton = ctk.CTkButton(changeNameFrame, text="Submit", font=font(18), command=submit, fg_color="#0f1010", hover_color="#0f1010", text_color="white")
        submitButton.place(relx=0.5, rely=0.85, anchor="center")
        submitButton.bind("<Enter>", on_enter)
        submitButton.bind("<Leave>", on_leave)

        

    reportButton = ctk.CTkButton(root, text="   Change project name", font=font(15), fg_color= color, command=changeName, hover_color=color)
    reportButton.place(relx=.008, rely=.095, anchor="nw")
    reportButton.bind("<Enter>", on_enter)
    reportButton.bind("<Leave>", on_leave)

    #=========================== welcomes user to home page ======================================================================================================================================================
    labelText = ctk.CTkLabel(detailedProjectFrame, text="Project name: " + name, font=font(20), fg_color=color, text_color="white")
    labelText.place(relx=0.02, rely=0.05, anchor="w")