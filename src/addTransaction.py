#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
#from tkcalendar import Calendar


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

#=========================== function for button highlighting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

check = 0

#=========================== function to create add item frame ======================================================================================================================================================
def addTransaction(root, listbox, tempLabel, user):
#=========================== add organization frame ======================================================================================================================================================
    transactionInfo = db[user]
    global check
    if check == 0:
        check = 1
        addTransactionFrame = ctk.CTkFrame(root, width=500, height=600, fg_color=color, border_color="#1e2121", border_width=4)
        addTransactionFrame.place(relx=1, rely=0, anchor="ne")
        addTransactionFrame.focus_set()

        def back():
            global check
            addTransactionFrame.place_forget()
            check = 0

        backButton = ctk.CTkButton(addTransactionFrame, text="x", font=font(20), command=back, fg_color=color, hover_color=color, width=0, height=0)
        backButton.place(relx=.04, rely=0.02, anchor="nw")
        backButton.bind("<Enter>", on_enter)
        backButton.bind("<Leave>", on_leave)

        amountEntryText = ctk.CTkLabel(addTransactionFrame, text="Enter Amount", font=font(15), fg_color=color, text_color="white")
        amountEntryText.place(relx=0.12, rely=0.15, anchor="w")

        amountEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Amount", width=400, height=40, justify="center", fg_color=color, text_color="white")
        amountEntry.place(relx=0.5, rely=0.2, anchor="center")

        categoryText = ctk.CTkLabel(addTransactionFrame, text="Category", font=font(15), fg_color=color, text_color="white")
        categoryText.place(relx=0.12, rely=0.35, anchor="w")
        categoryFrame = ctk.CTkFrame(
            addTransactionFrame,
            width=400,
            height=40,
            fg_color=color,
            border_color="#565B5E",  # Match border color of other entries
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
        categoryDropdown.set("Select a category")  # Set default option

        dateText = ctk.CTkLabel(addTransactionFrame, text="Date", font=font(15), fg_color=color, text_color="white")
        dateText.place(relx=0.12, rely=0.55, anchor="w")
        
        dateEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Enter a date", width=400, height=40, justify="center", fg_color=color, text_color="white", state="normal")
        dateEntry.place(relx=0.5, rely=0.6, anchor="center")

        optionalInfoText = ctk.CTkLabel(addTransactionFrame, text="Enter Any Extra Information", font=font(15), fg_color=color, text_color="white")
        optionalInfoText.place(relx=0.12, rely=0.75, anchor="w")

        optionalInfoEntry = ctk.CTkEntry(addTransactionFrame, font=font(15), placeholder_text="Optional Info", width=400, height=40, justify="center", fg_color=color, text_color="white")
        optionalInfoEntry.place(relx=0.5, rely=0.8, anchor="center")

        def submit():
            global check
            orgs = transactionInfo.find()
            date = list(dateEntry.get())
            try:
                float(amountEntry.get())
            except:
                error("Make Sure The Amount Is a Numerical Value", root)

            try:
                float(date[0])
                float(date[1])
                float(date[3])
                float(date[4])
                float(date[6])
                float(date[7])
                float(date[8])
                float(date[9])
            except:
                error("Please Enter A Valid Date", root)

            if amountEntry.get() == "" or dateEntry.get() == "" or categoryDropdown.get() == "" or optionalInfoEntry.get() == "":
                error("One or More Fields Are Empty, Please Use N/A In Replacement Of An Empty Entry", root)

            elif float(amountEntry.get()) > 1000000:
                error("Amount Is Too Large, Please Enter A Smaller Amount", root)

            elif len(date) != 10:
                error("Please Enter A Valid Date", root)

            elif date[2] != "/" or date[5] != "/":
                error("Please Enter A Valid Date", root)  

            elif len(optionalInfoEntry.get()) > 25:
                error("Please Enter A Shorter Description", root)
            else:
                check = 0
                transactionInfo.insert_one({"amount": round(float(amountEntry.get()), 2), "resources": categoryDropdown.get(), "Date": dateEntry.get(), "extraInfo": optionalInfoEntry.get()})
                addTransactionFrame.place_forget()
                count = 0
                for item in listbox.get_children():
                    listbox.delete(item)
                for item in orgs:
                    listbox.insert(parent='', index='end', text="", iid=count, values=(item["amount"], item["resources"], item["Date"], item["extraInfo"]))
                    count += 1
                transactions = transactionInfo.find()
                total = 0
                for transaction in transactions:
                    if transaction["resources"] == "Income":
                        total += transaction["amount"]
                    else:
                        total -= transaction["amount"]

                tempLabel.configure(text= "Total: " + str(total))

                success("Transaction Was Succesfully Added To The Database!", root)

        submitButton = ctk.CTkButton(addTransactionFrame, text="Submit", font=font(18), command=submit, fg_color=color, hover_color=color, text_color="white")
        submitButton.place(relx=0.5, rely=0.9, anchor="center")
        submitButton.bind("<Enter>", on_enter)
        submitButton.bind("<Leave>", on_leave)
    else:
        error("Please Close The Existing 'Add Organization' Page First", root)


