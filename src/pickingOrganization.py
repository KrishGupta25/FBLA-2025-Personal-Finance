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
from addItem import addItem
from editItem import editItem
from removeItem import removeItem
from filter import filter
from report import report
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
def pickingOrg(root, email):

#=========================== find users preferred name ======================================================================================================================================================
    temp = loginInfo.find({"email": email})
    orgs = transactionInfo.find()
    for item in temp:
        user = item["preferredName"]

#=========================== home page frame ======================================================================================================================================================
    pickingFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    pickingFrame.place(relx= 0, rely= 0)

#=========================== welcomes user to home page ======================================================================================================================================================
    labelText = ctk.CTkLabel(pickingFrame, text="Welcome " + user, font=font(20), fg_color=color, text_color="white")
    labelText.place(relx=0.02, rely=0.05, anchor="w")

#=========================== listbox style ======================================================================================================================================================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground= color, background = color, foreground= "white", font= ("Quicksand", 12), rowheight= 100, highlightbackground = color, highlightcolor= accent)
    style.configure("Treeview.Heading", background = color, foreground= "white", borderwidth= 0, font= ("Quicksand", 12))
    style.map('Treeview', background=[('selected', '#292929')])

#=========================== create listbox ======================================================================================================================================================
    listbox = ttk.Treeview(pickingFrame, selectmode="extended",columns=("c1", "c2", "c3", "c4"),show="headings", height= 5)
    listbox.column("# 1", anchor="center", width = 360)
    listbox.heading("# 1", text="Name")
    listbox.column("# 2", anchor="center", width = 360)
    listbox.heading("# 2", text="Resources")
    listbox.column("# 3", anchor="center", width = 360)
    listbox.heading("# 3", text="Location")
    listbox.column("# 4", anchor="center", width = 360)
    listbox.heading("# 4", text="Contact")

    listbox.place(relx=.5, rely=.5, anchor="center")

#=========================== add/edit/remove/view organization buttons ======================================================================================================================================================
    addOrgButton = ctk.CTkButton(pickingFrame, text="Add Organization", font=font(18), command = lambda:[addItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    addOrgButton.place(relx=0.2, rely=0.91, anchor="center")
    addOrgButton.bind("<Enter>", on_enter)
    addOrgButton.bind("<Leave>", on_leave)

    editOrgButton = ctk.CTkButton(pickingFrame, text="Edit Organization", font=font(18), command = lambda:[editItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    editOrgButton.place(relx=0.4, rely=0.91, anchor="center")
    editOrgButton.bind("<Enter>", on_enter)
    editOrgButton.bind("<Leave>", on_leave)

    removeOrgButton = ctk.CTkButton(pickingFrame, text="Remove Organization", font=font(18), command = lambda:[removeItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    removeOrgButton.place(relx=0.6, rely=0.91, anchor="center")
    removeOrgButton.bind("<Enter>", on_enter)
    removeOrgButton.bind("<Leave>", on_leave)

    #=========================== create report button ======================================================================================================================================================
    reportButton = ctk.CTkButton(pickingFrame, text="   Create Report", font=font(15), fg_color= color, command=lambda:(report(pickingFrame, moreFrame)), hover_color=color)
    reportButton.place(relx=.008, rely=.095, anchor="nw")
    reportButton.bind("<Enter>", on_enter)
    reportButton.bind("<Leave>", on_leave)

    count = 0
    for item in listbox.get_children():
        listbox.delete(item)
    for item in orgs:
        listbox.insert(parent='', index='end', text= "", iid= count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
        count+= 1

    searchLabel = ctk.CTkLabel(pickingFrame, text= "🔎", font=font(20), fg_color=color, text_color="white")
    searchLabel.place(relx=0.31, rely=0.075, anchor="center")

    searchEntry = ctk.CTkEntry(pickingFrame, font= font(15), width= 400, height= 20, justify= "left", placeholder_text="Search by name", fg_color=color, text_color="white")
    searchEntry.place(relx= 0.5, rely= 0.075, anchor= "center")
    final = list()

    def on_key_press(event):
        check = 0
        orgs = transactionInfo.find()
        search= searchEntry.get()
        if len(list(search)) > 0:
            final.clear()
            for item in orgs:
                name = item["orgName"]
                newName = name[:len(list(search))]
                if len(list(search)) <= len(list(name)):
                    # not case sensitive search
                    if search == newName or search.capitalize() == newName:
                        final.append(item)

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
                listbox.insert(parent='', index='end', text= "", iid= count, values=(item["orgName"], item["resources"], item["location"], item["contactInfo"]))
                count+= 1

    
    searchEntry.bind("<KeyRelease>", on_key_press)
          
    filterButton = ctk.CTkButton(pickingFrame, text="filter", font=font(15), command= lambda:(filter(pickingFrame, listbox)), fg_color=accent, hover_color="#63C28D", text_color=color)
    filterButton.place(relx=0.7, rely=0.075, anchor="center")

    

#=========================== find users first and last name ======================================================================================================================================================
    temp = loginInfo.find({"email": email})
    for item in temp:
        first = item["firstName"]
        last = item["lastName"]
        name = f'{first} {last}'

#=========================== create pop up window for more options ======================================================================================================================================================
    def more():
        def account():
            moreFrame.place_forget()

#=========================== get all user data ======================================================================================================================================================
            temp = loginInfo.find({"email": email})
            for item in temp:
                first = item["firstName"]
                last = item["lastName"]
                preferred = item["preferredName"]
                password = item["password"]
                
#=========================== create account frame ======================================================================================================================================================
            accountFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            accountFrame.place(relx= 0, rely= 0, anchor= "nw")

            accountlabel = ctk.CTkLabel(accountFrame, text="Acount Details", font=font(35), fg_color=color, text_color="white")
            accountlabel.place(relx=0.5, rely=0.02, anchor="n")

#=========================== password entry ======================================================================================================================================================
            passwordLabel2 = ctk.CTkLabel(accountFrame, text="Password", font=font(15), fg_color=color, text_color="white")
            passwordLabel2.place(relx=0.335, rely=0.16, anchor="nw")
            
            passwordEntry2 = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center", fg_color=color, text_color="white")
            passwordEntry2.place(relx= 0.5, rely= 0.25, anchor= "center")
            passwordEntry2.insert(0, password)
            passwordEntry2.bind('<FocusIn>', lambda x: passwordEntry2.select_range(0, "end"))

#=========================== first name entry ======================================================================================================================================================
            firstNameLabel = ctk.CTkLabel(accountFrame, text="First Name", font=font(15), fg_color=color, text_color="white")
            firstNameLabel.place(relx=0.335, rely=0.33, anchor="nw")
            
            firstNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center", fg_color=color, text_color="white")
            firstNameEntry.place(relx= 0.5, rely= 0.42, anchor= "center")
            firstNameEntry.insert(0, first)
            firstNameEntry.bind('<FocusIn>', lambda x: firstNameEntry.select_range(0, "end"))

#=========================== last name entry ======================================================================================================================================================
            lastNameLabel = ctk.CTkLabel(accountFrame, text="Last Name", font=font(15), fg_color=color, text_color="white")
            lastNameLabel.place(relx=0.335, rely=0.5, anchor="nw")
            
            lastNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center", fg_color=color, text_color="white")
            lastNameEntry.place(relx= 0.5, rely= 0.59, anchor= "center")
            lastNameEntry.insert(0, last)
            lastNameEntry.bind('<FocusIn>', lambda x: lastNameEntry.select_range(0, "end"))

#=========================== preferred name entry ======================================================================================================================================================
            preferredNameLabel = ctk.CTkLabel(accountFrame, text="Preferred Name", font=font(15), fg_color=color, text_color="white")
            preferredNameLabel.place(relx=0.335, rely=0.67, anchor="nw")
            
            preferredNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center", fg_color=color, text_color="white")
            preferredNameEntry.place(relx= 0.5, rely= 0.76, anchor= "center")
            preferredNameEntry.insert(0, preferred)
            preferredNameEntry.bind('<FocusIn>', lambda x: preferredNameEntry.select_range(0, "end"))

            backButton = ctk.CTkButton(accountFrame, text="⌂", font=font(40), command= accountFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== password check ======================================================================================================================================================
            def confirm():
                #Checking to see if either entry is empty
                if passwordEntry2.get() == "":
                    error("Either one or more of the required fields are empty or your entry has spaces", accountFrame)

                #Checking to see if either entry has spaces
                elif passwordEntry2.get().find(" ") > -1:
                    error("Either one or more of the required fields are empty or your entry has spaces", accountFrame)

                #Checking to see if there is at least one uppercase character in the password
                elif any(ele.isupper() for ele in passwordEntry2.get()) == False:
                    error("There is no uppercase letter in your password, please try again!", accountFrame)
                
                #Checking to see if there is at least one lowercase character in the password
                elif any(ele.islower() for ele in passwordEntry2.get()) == False:
                    error("There is no lowercase letter in your password, please try again!", accountFrame)
            
                #Checking to see if there is at least one special character in the password
                elif (passwordEntry2.get().isalnum()) == True:
                    error("There is no special characters in your password, please try again!", accountFrame)

                #Checking to see if there is at least one number in the password
                elif any(ele.isdigit() for ele in passwordEntry2.get()) == False:
                    error("There is no number in your password, please try again!", accountFrame)
                
                #Checking to see if there is at least 8 characters in the password
                elif len(passwordEntry2.get()) <= 8:
                    error("There arent 8 characters in your password, please try again!", accountFrame)

                #If all of those checks are passed then replace all the changed values
                else:
                    loginInfo.replace_one({"email": email}, {"email": email, "password": passwordEntry2.get(), "firstName": firstNameEntry.get(), "lastName": lastNameEntry.get(), "preferredName": preferredNameEntry.get()})
                    confirmLabel = ctk.CTkLabel(accountFrame, text="*all changes have been saved, please log out for changes to take effect", font=font(15), text_color=accent, fg_color=color)
                    confirmLabel.place(relx=0.5, rely=.83, anchor="center")
                


            confirmButton = ctk.CTkButton(accountFrame, text="Confirm", font=font(25), command = confirm, fg_color=color, hover_color=color)
            confirmButton.place(relx=0.5, rely=0.9, anchor="center")
            confirmButton.bind("<Enter>", on_enter)
            confirmButton.bind("<Leave>", on_leave)

#=========================== create security frame over account frame ======================================================================================================================================================
            securityFrame = ctk.CTkFrame(accountFrame, width=1200, height=600, fg_color= color, bg_color= color)
            securityFrame.place(relx= 0, rely= 0, anchor= "nw")

            back1Button = ctk.CTkButton(securityFrame, text="⌂", font=font(40), command= lambda: [securityFrame.place_forget(), accountFrame.place_forget()], fg_color=color, hover_color=color, width=0, height=0)
            back1Button.place(relx=.02, rely=0.001, anchor="nw")
            back1Button.bind("<Enter>", on_enter)
            back1Button.bind("<Leave>", on_leave)

            securityFramelabel = ctk.CTkLabel(securityFrame, text="Please Confirm Your Identity", font=font(35), fg_color=color, text_color="white")
            securityFramelabel.place(relx=0.5, rely=0.02, anchor="n")


            securitylabel = ctk.CTkLabel(securityFrame, text="Password", font=font(15), fg_color=color, text_color="white")
            securitylabel.place(relx=0.34, rely=0.42, anchor="nw")

            passwordEntry = ctk.CTkEntry(securityFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*", fg_color=color, text_color="white")
            passwordEntry.place(relx= 0.5, rely= 0.5, anchor= "center")

#=========================== function for submittion ======================================================================================================================================================
            def submit():
                entry = passwordEntry.get()
                values = loginInfo.find({'email': email})
                for x in values:
                    if x['password'] == entry:
                        securityFrame.place_forget()
                    else:
                        error("Incorrect password please try again", securityFrame)

#=========================== create submittion button ======================================================================================================================================================
            submitButton = ctk.CTkButton(securityFrame, text="Submit", font=font(18), command = submit, fg_color=color, hover_color=color)
            submitButton.place(relx=0.5, rely=0.6, anchor="center")
            submitButton.bind("<Enter>", on_enter)
            submitButton.bind("<Leave>", on_leave)


#=========================== create account button ======================================================================================================================================================
        accountButton = ctk.CTkButton(moreFrame, text="   Account", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command = account)
        accountButton.place(relx=0, rely=0, anchor="nw")

#=========================== create settings page ======================================================================================================================================================
        def settings():
            moreFrame.place_forget()

            settingFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            settingFrame.place(relx= 0, rely= 0, anchor= "nw")

            settingslabel = ctk.CTkLabel(settingFrame, text="Settings", font=font(35), fg_color=color, text_color="white")
            settingslabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(settingFrame, text="⌂", font=font(40), command= settingFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== create about frame ======================================================================================================================================================
        def about():
            moreFrame.place_forget()
            aboutFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            aboutFrame.place(relx= 0, rely= 0, anchor= "nw")

            AboutUslabel = ctk.CTkLabel(aboutFrame, text="About Us ", font=font(35), fg_color=color, text_color="white")
            AboutUslabel.place(relx=0.5, rely=0.02, anchor="n")

            AboutUstext = ctk.CTkLabel(aboutFrame, text="""Welcome to our Future Business Leaders of America (FBLA) Programming and Coding project for 2023-2024! We, Harishankar Rajesh and
            \nKrish Gupta, are juniors at River Ridge High School and have spent the last two months developing a busniness/orginization storage platform. 
            \nOur system is designed to be able to easily add, store, view, edit, remove, seach, and filter businesses while also implementing a 
            \nfriendly and effecient UI.This project involved in-depth learning of various software development facets, while also enhancing our
            \nability to devise effective solutions to complex problems. The journey was challenging but rewarding, with the final product serving as 
            \nboth a tool for fostering a more interactive educational environment and a testament to our journey into the world of programming. 
            \nfireplaypus375@gmail.com (Haris Rajesh) 
            \nkrishgupta2025@gmail.com(Krish Gupta) 
            \nGithub: https://github.com/HarisR39/CTE_Partner_Pro""", font=font(17), fg_color=color, text_color="white")
            AboutUstext.place(relx=0.5, rely=0.55, anchor="center")

            backButton = ctk.CTkButton(aboutFrame, text="⌂", font=font(40), command= aboutFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== create about button ======================================================================================================================================================
        aboutButton = ctk.CTkButton(moreFrame, text="   About", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= about)
        aboutButton.place(relx=0, rely=.33, anchor="nw")

#=========================== create about frame ======================================================================================================================================================
        def support():
            moreFrame.place_forget()
            supportFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            supportFrame.place(relx= 0, rely= 0, anchor= "nw")

            supportlabel = ctk.CTkLabel(supportFrame, text="Support page", font=font(35), fg_color=color, text_color="white")
            supportlabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(supportFrame, text="⌂", font=font(40), command= supportFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

            # Create an object of tkinter ImageTk
            def resource_path(relative_path):
                """ Get absolute path to resource, works for dev and for PyInstaller """
                try:
                    # PyInstaller creates a temp folder and stores path in _MEIPASS
                    base_path = sys._MEIPASS
                except Exception:
                    base_path = os.path.abspath(".")

                return os.path.join(base_path, relative_path)
            imgage = Image.open(resource_path("./src/loginImage.png"))
            new_img = imgage.resize((1200,600))
            img = ImageTk.PhotoImage(new_img)


            # Create a Label Widget to display the text or Image
            label = ctk.CTkLabel(supportFrame, image = img, text="")
            label.place(relx= 0.5, rely= 0.5, anchor= "center")

            def suport2(destroy):
                supportFrame2 = ctk.CTkFrame(supportFrame, width=1200, height=600, fg_color= color, bg_color= color)
                supportFrame2.place(relx= 0, rely= 0, anchor= "nw")

                supportlabel = ctk.CTkLabel(supportFrame2, text="Support page", font=font(35), fg_color=color, text_color="white")
                supportlabel.place(relx=0.5, rely=0.02, anchor="n")

                def back():
                    destroy.place_forget()
                    supportFrame2.place_forget()

                backButton = ctk.CTkButton(supportFrame2, text="⌂", font=font(40), command= back, fg_color=color, hover_color=color, width=0, height=0)
                backButton.place(relx=.02, rely=0.001, anchor="nw")
                backButton.bind("<Enter>", on_enter)
                backButton.bind("<Leave>", on_leave)

                # Create an object of tkinter ImageTk
                
                def resource_path(relative_path):
                    """ Get absolute path to resource, works for dev and for PyInstaller """
                    try:
                        # PyInstaller creates a temp folder and stores path in _MEIPASS
                        base_path = sys._MEIPASS
                    except Exception:
                        base_path = os.path.abspath(".")

                    return os.path.join(base_path, relative_path)
                imgage = Image.open(resource_path("./src/mainImage.png"))
                new_img = imgage.resize((1200,600))
                img = ImageTk.PhotoImage(new_img)

                # Create a Label Widget to display the text or Image
                label = ctk.CTkLabel(supportFrame, image = img, text="")
                label.place(relx= 0.5, rely= 0.5, anchor= "center")

            nextButton = ctk.CTkButton(supportFrame, text="Next", font=font(25), command= lambda:(suport2(supportFrame)), fg_color=color, hover_color=color, width=0)
            nextButton.place(relx=.5, rely=0.95, anchor="center")
            nextButton.bind("<Enter>", on_enter)
            nextButton.bind("<Leave>", on_leave)

#=========================== create support button ======================================================================================================================================================
        #supportButton = ctk.CTkButton(moreFrame, text="   Support", font=font(15), command= support, fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0)
        #supportButton.place(relx=0, rely=.6, anchor="nw")

#=========================== function to logout ======================================================================================================================================================
        def logout():
            moreFrame.place_forget()
            pickingFrame.place_forget()

#=========================== create logout button ======================================================================================================================================================
        logOutButton = ctk.CTkButton(moreFrame, text="   Log out", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= logout)
        logOutButton.place(relx=0, rely=.66, anchor="nw")

#=========================== algorithm to open and close more frame ======================================================================================================================================================
        if moreFrame.winfo_ismapped():
            moreFrame.place_forget()
        else:
            moreFrame.place(relx= .975, rely= .08, anchor= "ne")

#=========================== create more frame ======================================================================================================================================================
    moreFrame = ctk.CTkFrame(pickingFrame, width= 187.5, height= 150, fg_color= "#1e2121")

#=========================== create button to open up the more frame ======================================================================================================================================================
    moreButton = ctk.CTkButton(pickingFrame, text=name, font=font(18), command= more, fg_color=color, hover_color=color, width=0)
    moreButton.place(relx=.975, rely=0.05, anchor="e")
    moreButton.bind("<Enter>", on_enter)
    moreButton.bind("<Leave>", on_leave)

