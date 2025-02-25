import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient

#=========================== Import Required Functions ===========================
from errorPage import error
from signUp import signUp
from HomePage import pickingTransaction
from tkinter import font

#=========================== Establish Connection to Database ===========================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#=========================== Custom Font Function ===========================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

def font(size):
    return ("Quicksand", size)

#=========================== Set Default Colors ===========================
color = "#121414"
accent = "#3cb371"

#=========================== Button Highlight Functions ===========================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

#=========================== Create Main Frame ===========================
mainFrame = ctk.CTk(fg_color=color)
mainFrame.geometry("1200x600+180+120")
#mainFrame.resizable(width=False, height=False)

#=========================== Create Login Frame ===========================
loginFrame = ctk.CTkFrame(mainFrame, fg_color=color)
loginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

#=========================== Create Login Title ===========================
loginLabel = ctk.CTkLabel(loginFrame, text="Log in to BudgetBuddy", font=font(50), fg_color=color, text_color="white")
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#=========================== Create Email Entry Box ===========================
emailEntry = ctk.CTkEntry(loginFrame, font=font(15), placeholder_text="Name@domain.com", justify="center", fg_color=color, text_color="white")
emailEntry.place(relx=0.5, rely=0.45, relwidth=0.33, relheight=0.07, anchor="center")

emailLabel = ctk.CTkLabel(loginFrame, text="Email", font=font(15), fg_color=color, text_color="white")
emailLabel.place(relx=0.335, rely=0.36, anchor="nw")

#=========================== Create Password Entry Box ===========================
passwordEntry = ctk.CTkEntry(loginFrame, font=font(15), placeholder_text="Password", justify="center", show="*", fg_color=color, text_color="white")
passwordEntry.place(relx=0.5, rely=0.6, relwidth=0.33, relheight=0.07, anchor="center")

passwordLabel = ctk.CTkLabel(loginFrame, text="Password", font=font(15), fg_color=color, text_color="white")
passwordLabel.place(relx=0.335, rely=0.51, anchor="nw")

#=========================== Login Function ===========================
def login():
    count = 0
    temp = loginInfo.find()
    for item in temp:
        if str(item['email']) == str(emailEntry.get()) and str(item['password']) == str(passwordEntry.get()):
            count += 1

    if count == 1:
        pickingTransaction(loginFrame, emailEntry.get())
        emailEntry.delete(0, "end")
        passwordEntry.delete(0, "end")
    else:
        error("Wrong Email or Password! If You Don't Have An Account, Click The Sign Up button!", loginFrame)
        emailEntry.delete(0, "end")
        passwordEntry.delete(0, "end")

#=========================== Create Login Button ===========================
loginButton = ctk.CTkButton(loginFrame, text="Log in to BudgetBuddy", font=font(25), command=login, fg_color=accent, hover_color="#63C28D", text_color=color)
loginButton.place(relx=0.5, rely=0.825, relwidth=0.25, relheight=0.08, anchor="center")

#=========================== Create Sign Up Button ===========================
signupButton = ctk.CTkButton(loginFrame, text="Sign up for BudgetBuddy", font=font(18), command=lambda: signUp(loginFrame), fg_color=color, hover_color=color)
signupButton.place(relx=0.5, rely=0.92, relwidth=0.25, relheight=0.06, anchor="center")
signupButton.bind("<Enter>", on_enter)
signupButton.bind("<Leave>", on_leave)

#=========================== Show Password Checkbox ===========================
def showPasswordCommand():
    if passwordEntry.cget('show') == '':
        passwordEntry.configure(show='*')
    else:
        passwordEntry.configure(show='')

showPasswordCheckbox = ctk.CTkCheckBox(loginFrame, text="Show Password", command=showPasswordCommand, hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white")
showPasswordCheckbox.place(relx=0.335, rely=0.65, relwidth=0.2, relheight=0.05)

#=========================== Run GUI ===========================
mainFrame.mainloop()