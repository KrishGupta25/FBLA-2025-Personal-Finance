#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
from detailedProjectPage import detailedProject

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
def Projects(root, email):

#=========================== find users preferred name and transaction details =================================================================================================================================
    temp = loginInfo.find({"email": email})
    for item in temp:
        user = item["preferredName"]
        pickingTransactionId = item["_id"]
    
    transactionInfo = db[str(pickingTransactionId)+"collection"]
    transactions = transactionInfo.find()

#=========================== home page frame ======================================================================================================================================================
    projectsFrame = ctk.CTkFrame(root, width= 1050, height= 600, fg_color= color)
    projectsFrame.place(relx= 0.125, rely= 0, anchor= "nw")

#=========================== welcomes user to home page ======================================================================================================================================================
    labelText = ctk.CTkLabel(projectsFrame, text="Welcome, " + user, font=font(20), fg_color=color, text_color="white")
    labelText.place(relx=0.5, rely=0.05, anchor="center")

#=========================== listbox style ======================================================================================================================================================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= color, background = color, foreground= "white", font= ("Quicksand", 12), rowheight= 100, highlightbackground = color, highlightcolor= accent)
    style.configure("Treeview.Heading", background = color, foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    style.map('Treeview', background=[('selected', '#292929')])

#=========================== create project storage boxes ======================================================================================================================================================
    projectNamesData = db[str(pickingTransactionId) + "projectNames"]
    projectNames = projectNamesData.find()
    projectNamesList = []
    for project in projectNames:
        projectNamesList.append(project["projectName"])
    columns = 4
    rows = 3

    for i in range(12):
        row = i // columns  # Row index (0, 1, 2)
        col = i % columns   # Column index (0, 1, 2, 3)

        relx = (col + 1) / (columns + 1)  # Even spacing in X
        rely = (row + 1) / (rows + 1)     # Even spacing in Y

        button = ctk.CTkButton(
            projectsFrame,
            text=projectNamesList[i],
            font=(font(18)),
            fg_color="#0f1010",
            hover_color="#2a2e2e",
            width=175,
            height=100,
            corner_radius=0,
            anchor="center",
            command=lambda i=i: detailedProject(projectsFrame, email, str(i))
        )
        button.place(relx=relx, rely=rely, anchor="center")

    

                
