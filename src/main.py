#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient

#=========================== import all required functions ======================================================================================================================================================
from errorPage import error
from signUp import signUp
from pickingTransaction import pickingTransaction
from tkinter import font

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

#=========================== cunction for button highliting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

#=========================== creates main frame ======================================================================================================================================================
mainFrame = ctk.CTk(fg_color=color)
mainFrame.geometry("1200x600+180+120")
mainFrame.resizable(width=False, height=False)


#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#=========================== ALL OF THE LOGIN PAGE STUFF ======================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================

#=========================== Creating a blank page or "frame" on top of the main one to work on for the login page ======================================================================================================================================================
loginFrame = ctk.CTkFrame(mainFrame, width=1200, height=600, fg_color=color)
loginFrame.place(relx=0, rely=0)

#=========================== Creating title text that says "Login to BudgetBuddy" ======================================================================================================================================================
loginLabel = ctk.CTkLabel(loginFrame, text="Log in to BudgetBuddy", font=font(50), fg_color=color, text_color="white")
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#=========================== Creating a email entry box and the text above it ======================================================================================================================================================
# Text box
emailEntry = ctk.CTkEntry(loginFrame, font=font(15), placeholder_text="Name@domain.com", width=400, height=40, justify="center", fg_color=color, text_color="white")
emailEntry.place(relx=0.5, rely=0.45, anchor="center")
# Text above text box
emailLabel = ctk.CTkLabel(loginFrame, text="Email", font=font(15), fg_color=color, text_color="white")
emailLabel.place(relx=0.335, rely=0.36, anchor="nw")

#=========================== Creating a password entry box and the text above it ======================================================================================================================================================
# Text box
passwordEntry = ctk.CTkEntry(loginFrame, font=font(15), placeholder_text="Password", width=400, height=40, justify="center", show="*", fg_color=color, text_color="white")
passwordEntry.place(relx=0.5, rely=0.6, anchor="center")
# Text above text box
passwordLabel = ctk.CTkLabel(loginFrame, text="Password", font=font(15), fg_color=color, text_color="white")
passwordLabel.place(relx=0.335, rely=0.51, anchor="nw")

#============ Making sure that the email and the password is valid in our database =============================================================================================================================
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

#=========================== Login Button ======================================================================================================================================================
loginButton = ctk.CTkButton(loginFrame, text="Log in to BudgetBuddy", font=font(25), command=lambda: (login()), fg_color=accent, hover_color="#63C28D", text_color=color)
loginButton.place(relx=0.5, rely=0.825, anchor="center")

''' - WORK IN PROGRESS
#=========================== Light and Dark Mode Button ======================================================================================================================================================
switch_var = ctk.StringVar(value="on")
def backgroundColor(root):

    if switch_var.get() == "on": #root.cget('fg_color') == "#121414":
        color = "white"
        print(1)
    elif switch_var.get() == "off":  #root.cget('fg_color') == "white":
        color = "#121414"
        print(0)

    root.configure(fg_color = color)

lightAndDarkSwitch = ctk.CTkSwitch(loginFrame, command = lambda:(backgroundColor(loginFrame)), onvalue= "on", offvalue= "off", variable= switch_var, text = "hola")
lightAndDarkSwitch.place(relx = 0.5, rely = 0.5)
'''
#=========================== Sign up Button ======================================================================================================================================================
signupButton = ctk.CTkButton(loginFrame, text="Sign up for BudgetBuddy", font=font(18), command=lambda: (signUp(loginFrame)), fg_color=color, hover_color=color)
signupButton.place(relx=0.5, rely=0.92, anchor="center")
signupButton.bind("<Enter>", on_enter)
signupButton.bind("<Leave>", on_leave)

#=========================== Password Checkbox ======================================================================================================================================================
def showPasswordCommand():
    if passwordEntry.cget('show') == '':
        passwordEntry.configure(show='*')
    else:
        passwordEntry.configure(show='')

showPasswordCheckbox = ctk.CTkCheckBox(loginFrame, text="Show Password", command=showPasswordCommand, hover_color=accent, checkmark_color=accent, font=font(12), fg_color=color, text_color="white")
showPasswordCheckbox.place(relx=0.335, rely=0.65)

#=========================== Keeps GUI Running ======================================================================================================================================================
mainFrame.mainloop()