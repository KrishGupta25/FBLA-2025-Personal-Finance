#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
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

#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== cunction for button highliting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'


#=========================== function to create edit item frame ======================================================================================================================================================
def removeItem(root, listbox,tempLabel, user, switch, projectid):

    query = {
        "$or": [
            # Condition for string _id
            { "_id": { "$type": "string", "$regex": str(user)+"projectNames"+ str(projectid)}},
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



    transactionInfo = db[user]
    temp = listbox.selection()
    delete = list()
    if len(temp) == 0:
        error("Please Select At Least One Transaction To Delete", root)
    else:
        if switch == 0:
            orgs = transactionInfo.find()
        else:
            orgs = transactionInfo.find(query)
        selection = list()
        for item in temp:
            selection.append(listbox.item(item, option="values"))
        for select in selection:
            for org in orgs:
                if float(select[0]) == org["amount"] and select[1] == org["resources"] and select[2] == org["Date"] and select[3] == org["extraInfo"]:
                    delete.append({"amount": float(select[0]), "resources": select[1], "Date": select[2], "extraInfo": select[3]})
                    
        for item in delete:
            transactionInfo.delete_one(item)
            count = 0

        if switch == 0:
            orgs = transactionInfo.find()
        else:
            orgs = transactionInfo.find(query)
        count = 0
        for item in listbox.get_children():
            listbox.delete(item)
        for item in orgs:
            listbox.insert(parent='', index='end', text="", iid=count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
            count += 1

        if switch == 0:
            transactions = transactionInfo.find()
        else:
            transactions = transactionInfo.find(query)
        total = 0
        for transaction in transactions:
            if transaction["resources"] == "Income":
                total += transaction["amount"]
            else:
                total -= transaction["amount"]
            total = round(total, 2)

        tempLabel.configure(text= "Total: " + str(total))


        success("Transaction(s) Were Deleted", root)