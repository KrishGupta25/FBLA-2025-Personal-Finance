#Import all required dependencies
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import string

# Import all commands
from errorPage import error

#Creates connection to database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#Import custom font
pyglet.font.add_file('./assets/Quicksand-Bold.ttf')

#Function to simplify font size
def font(size):
    return ("Quicksand",size)

#Setting the default color
color = "#121414"
accent = "#3cb371"

def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

#Instantiatation of a new page for the signup
def pickingOrg(root, email):

    temp = loginInfo.find({"email": email})
    for item in temp:
        user = item["prefferedName"]

    #Create new info frame over "root" which in this case is "loginFrame"
    pickingFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    pickingFrame.place(relx= 0, rely= 0)

    labelText = ctk.CTkLabel(pickingFrame, text="Welcome " + user, font=font(30))
    labelText.place(relx=0.02, rely=0.05, anchor="w")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= color, background = color, foreground= "white", font= ("Quicksand", 12), rowheight= 120, highlightbackground = color, highlightcolor= accent)
    style.configure("Treeview.Heading", background = color, foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    style.map('Treeview', background=[('selected', '#292929')])

    listbox = ttk.Treeview(pickingFrame, selectmode="extended",columns=("c1", "c2", "c3"),show="headings", height= 5)
    listbox.column("# 1", anchor="center", width = 480)
    listbox.heading("# 1", text="Name")
    listbox.column("# 2", anchor="center", width = 480)
    listbox.heading("# 2", text="Type")
    listbox.column("# 3", anchor="center", width = 480)
    listbox.heading("# 3", text="Contact")

    listbox.place(relx=.5, rely=.53, anchor="center")

    temp = loginInfo.find({"email": email})
    for item in temp:
        first = item["firstName"]
        last = item["lastName"]
        name = f'{first} {last}'


    def more():
        def account():
            moreFrame.place_forget()

            accountFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            accountFrame.place(relx= 0, rely= 0, anchor= "nw")

            accountlabel = ctk.CTkLabel(accountFrame, text="Acount Details", font=font(35))
            accountlabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(accountFrame, text="⌂", font=font(40), command= accountFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

            securityFrame = ctk.CTkFrame(accountFrame, width=1200, height=600, fg_color= color, bg_color= color)
            securityFrame.place(relx= 0, rely= 0, anchor= "nw")

            back1Button = ctk.CTkButton(securityFrame, text="⌂", font=font(40), command= lambda: [securityFrame.place_forget(), accountFrame.place_forget()], fg_color=color, hover_color=color, width=0, height=0)
            back1Button.place(relx=.02, rely=0.001, anchor="nw")
            back1Button.bind("<Enter>", on_enter)
            back1Button.bind("<Leave>", on_leave)

            securityFramelabel = ctk.CTkLabel(securityFrame, text="Please Confirm Your Identity", font=font(35))
            securityFramelabel.place(relx=0.5, rely=0.02, anchor="n")


            securitylabel = ctk.CTkLabel(securityFrame, text="password", font=font(15))
            securitylabel.place(relx=0.34, rely=0.42, anchor="nw")

            passwordEntry = ctk.CTkEntry(securityFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
            passwordEntry.place(relx= 0.5, rely= 0.5, anchor= "center")

            def submit():
                entry = passwordEntry.get()
                values = loginInfo.find({'email': email})
                for x in values:
                    if x['password'] == entry:
                        securityFrame.place_forget()
                    else:
                        error("Incorrect password please try again", securityFrame)

            submitButton = ctk.CTkButton(securityFrame, text="submit", font=font(18), command = submit, fg_color=color, hover_color=color)
            submitButton.place(relx=0.5, rely=0.6, anchor="center")
            submitButton.bind("<Enter>", on_enter)
            submitButton.bind("<Leave>", on_leave)



        accountButton = ctk.CTkButton(moreFrame, text="   Account", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command = account)
        accountButton.place(relx=0, rely=0, anchor="nw")

        def settings():
            moreFrame.place_forget()

            settingFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            settingFrame.place(relx= 0, rely= 0, anchor= "nw")

            settingslabel = ctk.CTkLabel(settingFrame, text="Settings", font=font(35))
            settingslabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(settingFrame, text="⌂", font=font(40), command= settingFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

        settingsButton = ctk.CTkButton(moreFrame, text="   Settings", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command=settings)
        settingsButton.place(relx=0, rely=.2, anchor="nw")

        def about():
            moreFrame.place_forget()
            aboutFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            aboutFrame.place(relx= 0, rely= 0, anchor= "nw")

            AboutUslabel = ctk.CTkLabel(aboutFrame, text="About Us ", font=font(35))
            AboutUslabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(aboutFrame, text="⌂", font=font(40), command= aboutFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

        aboutButton = ctk.CTkButton(moreFrame, text="   about", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= about)
        aboutButton.place(relx=0, rely=.4, anchor="nw")

        supportButton = ctk.CTkButton(moreFrame, text="   Support", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0)
        supportButton.place(relx=0, rely=.6, anchor="nw")

        def logout():
            moreFrame.place_forget()
            pickingFrame.place_forget()

        logOutButton = ctk.CTkButton(moreFrame, text="   Log out", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= logout)
        logOutButton.place(relx=0, rely=.8, anchor="nw")

        if moreFrame.winfo_ismapped():
            moreFrame.place_forget()
        else:
            moreFrame.place(relx= .975, rely= .08, anchor= "ne")

    moreFrame = ctk.CTkFrame(pickingFrame, width= 187.5, height= 250, fg_color= "#1e2121")    

    moreButton = ctk.CTkButton(pickingFrame, text=name, font=font(18), command= more, fg_color=color, hover_color=color, width=0)
    moreButton.place(relx=.975, rely=0.05, anchor="e")
    moreButton.bind("<Enter>", on_enter)
    moreButton.bind("<Leave>", on_leave)

