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

check = 0

#=========================== function to create edit item frame ======================================================================================================================================================
def editItem(root, listbox, tempLabel):
#=========================== edit transaction frame ======================================================================================================================================================
    global check
    if check == 0:
        temp = listbox.selection()
        if len(temp) == 0:
            error("Please Select An Transaction To Edit", root)
        elif len(temp) > 1:
            error("You Can Only Select One Transaction To Edit At a Time", root)
        else:
            check = 1
            selection = listbox.item(temp, option="values")

            editItemFrame = ctk.CTkFrame(root, width=500, height=600, fg_color=color, border_color="#1e2121", border_width=4)
            editItemFrame.place(relx=1, rely=0, anchor="ne")
            editItemFrame.focus_set()

            def back():
                global check
                editItemFrame.place_forget()
                check = 0

            backButton = ctk.CTkButton(editItemFrame, text="x", font=font(20), command=back, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.04, rely=0.02, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

            labelText = ctk.CTkLabel(editItemFrame, text="Edit Transaction", font=font(20), fg_color=color, text_color="white")
            labelText.place(relx=0.5, rely=0.05, anchor="center")

            orgNameText = ctk.CTkLabel(editItemFrame, text="Amount", font=font(15), fg_color=color, text_color="white")
            orgNameText.place(relx=0.12, rely=0.15, anchor="w")

            orgNameEntry = ctk.CTkEntry(editItemFrame, font=font(15), width=400, height=40, justify="center", fg_color=color, text_color="white")
            orgNameEntry.place(relx=0.5, rely=0.2, anchor="center")
            orgNameEntry.insert(0, selection[0])
            orgNameEntry.bind('<FocusIn>', lambda x: orgNameEntry.select_range(0, "end"))

            categoryText = ctk.CTkLabel(editItemFrame, text="Category", font=font(15), fg_color=color, text_color="white")
            categoryText.place(relx=0.12, rely=0.35, anchor="w")

            categoryEntry = ctk.CTkEntry(editItemFrame, font=font(15), width=400, height=40, justify="center", fg_color=color, text_color="white")
            categoryEntry.place(relx=0.5, rely=0.4, anchor="center")
            categoryEntry.insert(0, selection[1])
            categoryEntry.bind('<FocusIn>', lambda x: categoryEntry.select_range(0, "end"))

            dateText = ctk.CTkLabel(editItemFrame, text="Date", font=font(15), fg_color=color, text_color="white")
            dateText.place(relx=0.12, rely=0.55, anchor="w")

            dateEntry = ctk.CTkEntry(editItemFrame, font=font(15), width=400, height=40, justify="center", fg_color=color, text_color="white")
            dateEntry.place(relx=0.5, rely=0.6, anchor="center")
            dateEntry.insert(0, selection[2])
            dateEntry.bind('<FocusIn>', lambda x: dateEntry.select_range(0, "end"))

            typeText = ctk.CTkLabel(editItemFrame, text="Additional Info", font=font(15), fg_color=color, text_color="white")
            typeText.place(relx=0.12, rely=0.75, anchor="w")

            typeEntry = ctk.CTkEntry(editItemFrame, font=font(15), width=400, height=40, justify="center", fg_color=color, text_color="white")
            typeEntry.place(relx=0.5, rely=0.8, anchor="center")
            typeEntry.insert(0, selection[3])
            typeEntry.bind('<FocusIn>', lambda x: typeEntry.select_range(0, "end"))

            def submit():
                global check
                orgs = transactionInfo.find()
                if orgNameEntry.get() == "" or dateEntry.get() == "" or categoryEntry.get() == "" or typeEntry.get() == "":
                    error("One or More Fields Are Empty, Please Use N/A In Replacement Of An Empty Entry", root)
                else:
                    transactionInfo.replace_one({"amount": int(selection[0]), "resources": selection[1], "Date": selection[2], "extraInfo": selection[3]}, {"amount": int(orgNameEntry.get()), "resources": categoryEntry.get(), "Date": dateEntry.get(), "extraInfo": typeEntry.get()})
                    editItemFrame.place_forget()
                    count = 0
                    for item in listbox.get_children():
                        listbox.delete(item)
                    for item in orgs:
                        listbox.insert(parent='', index='end', text="", iid=count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
                        count += 1
                    check = 0

                transactions = transactionInfo.find()
                total = 0
                for transaction in transactions:
                    if transaction["resources"] == "Income":
                        total += transaction["amount"]
                    else:
                        total -= transaction["amount"]

                tempLabel.configure(text= "Total: " + str(total))


                success("Transaction was succesfully edited", root)

            submitButton = ctk.CTkButton(editItemFrame, text="Submit", font=font(18), command=submit, fg_color=color, hover_color=color, text_color="white")
            submitButton.place(relx=0.5, rely=0.9, anchor="center")
            submitButton.bind("<Enter>", on_enter)
            submitButton.bind("<Leave>", on_leave)
    else:
        error("Please Close The Existing 'Edit Transaction' Page First", root)
