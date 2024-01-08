#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from addItem import addItem
from editItem import editItem
from removeItem import removeItem

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

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

#=========================== find users preffered name ======================================================================================================================================================
    temp = loginInfo.find({"email": email})
    orgs = orgInfo.find()
    for item in temp:
        user = item["prefferedName"]

#=========================== home page frame ======================================================================================================================================================
    pickingFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    pickingFrame.place(relx= 0, rely= 0)

#=========================== welcomes user to home page ======================================================================================================================================================
    labelText = ctk.CTkLabel(pickingFrame, text="Welcome " + user, font=font(30))
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

#=========================== add/edit/remove organization buttons ======================================================================================================================================================
    addOrgButton = ctk.CTkButton(pickingFrame, text="Add Organization", font=font(18), command = lambda:[addItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    addOrgButton.place(relx=0.25, rely=0.91, anchor="center")
    addOrgButton.bind("<Enter>", on_enter)
    addOrgButton.bind("<Leave>", on_leave)

    editOrgButton = ctk.CTkButton(pickingFrame, text="Edit Organization", font=font(18), command = lambda:[editItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    editOrgButton.place(relx=0.5, rely=0.91, anchor="center")
    editOrgButton.bind("<Enter>", on_enter)
    editOrgButton.bind("<Leave>", on_leave)

    removeOrgButton = ctk.CTkButton(pickingFrame, text="Remove Organization", font=font(18), command = lambda:[removeItem(pickingFrame, listbox)], fg_color=color, hover_color=color)
    removeOrgButton.place(relx=0.75, rely=0.91, anchor="center")
    removeOrgButton.bind("<Enter>", on_enter)
    removeOrgButton.bind("<Leave>", on_leave)

    count = 0
    for item in listbox.get_children():
        listbox.delete(item)
    for item in orgs:
        listbox.insert(parent='', index='end', text= "", iid= count, values= (item["orgName"], item["location"], item["resources"], item["contactInfo"]) )
        count+= 1

    searchLabel = ctk.CTkLabel(pickingFrame, text= "🔎", font=font(20))
    searchLabel.place(relx=0.31, rely=0.075, anchor="center")

    searchEntry = ctk.CTkEntry(pickingFrame, font= font(15), width= 400, height= 20, justify= "left", placeholder_text="Search by name")
    searchEntry.place(relx= 0.5, rely= 0.075, anchor= "center")
    final = list()

    def on_key_press(event):
        check = 0
        orgs = orgInfo.find()
        search= searchEntry.get()
        if len(list(search)) > 0:
            final.clear()
            for item in orgs:
                name = item["orgName"]
                newName = name[:len(list(search))]
                if len(list(search)) <= len(list(name)):
                    if search == newName:
                        final.append(item)

                count = 0
                for item in listbox.get_children():
                    listbox.delete(item)
                for item in final:
                    listbox.insert(parent='', index='end', text= "", iid= count, values= (item["orgName"], item["location"], item["resources"], item["contactInfo"]) )
                    count+= 1
        else:
            orgs = orgInfo.find()
            count = 0
            for item in listbox.get_children():
                listbox.delete(item)
            for item in orgs:
                listbox.insert(parent='', index='end', text= "", iid= count, values= (item["orgName"], item["location"], item["resources"], item["contactInfo"]) )
                count+= 1

    
    searchEntry.bind("<KeyRelease>", on_key_press)
    
            

    

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
                preferred = item["prefferedName"]
                password = item["password"]
                
#=========================== create account frame ======================================================================================================================================================
            accountFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            accountFrame.place(relx= 0, rely= 0, anchor= "nw")

            accountlabel = ctk.CTkLabel(accountFrame, text="Acount Details", font=font(35))
            accountlabel.place(relx=0.5, rely=0.02, anchor="n")

#=========================== password entry ======================================================================================================================================================
            passwordLabel2 = ctk.CTkLabel(accountFrame, text="Password", font=font(15))
            passwordLabel2.place(relx=0.335, rely=0.16, anchor="nw")
            
            passwordEntry2 = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center")
            passwordEntry2.place(relx= 0.5, rely= 0.25, anchor= "center")
            passwordEntry2.insert(0, first)
            passwordEntry2.bind('<FocusIn>', lambda x: passwordEntry2.select_range(0, "end"))

#=========================== first name entry ======================================================================================================================================================
            firstNameLabel = ctk.CTkLabel(accountFrame, text="First Name", font=font(15))
            firstNameLabel.place(relx=0.335, rely=0.33, anchor="nw")
            
            firstNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center")
            firstNameEntry.place(relx= 0.5, rely= 0.42, anchor= "center")
            firstNameEntry.insert(0, first)
            firstNameEntry.bind('<FocusIn>', lambda x: firstNameEntry.select_range(0, "end"))

#=========================== last name entry ======================================================================================================================================================
            lastNameLabel = ctk.CTkLabel(accountFrame, text="Last Name", font=font(15))
            lastNameLabel.place(relx=0.335, rely=0.5, anchor="nw")
            
            lastNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center")
            lastNameEntry.place(relx= 0.5, rely= 0.59, anchor= "center")
            lastNameEntry.insert(0, last)
            lastNameEntry.bind('<FocusIn>', lambda x: lastNameEntry.select_range(0, "end"))

#=========================== preffered name entry ======================================================================================================================================================
            preferredNameLabel = ctk.CTkLabel(accountFrame, text="Preferred Name", font=font(15))
            preferredNameLabel.place(relx=0.335, rely=0.67, anchor="nw")
            
            preferredNameEntry = ctk.CTkEntry(accountFrame, font= font(15), width= 400, height= 40, justify= "center")
            preferredNameEntry.place(relx= 0.5, rely= 0.76, anchor= "center")
            preferredNameEntry.insert(0, preferred)
            preferredNameEntry.bind('<FocusIn>', lambda x: preferredNameEntry.select_range(0, "end"))

            backButton = ctk.CTkButton(accountFrame, text="⌂", font=font(40), command= accountFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

            def confirm():
                print(passwordEntry2.get())
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
                    loginInfo.replace_one({"email": email}, {"email": email, "password": passwordEntry2.get(), "firstName": firstNameEntry.get(), "lastName": lastNameEntry.get(), "prefferedName": preferredNameEntry.get()})
                    confirmLabel = ctk.CTkLabel(accountFrame, text="*all changes have been saved", font=font(15), text_color=accent)
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

            securityFramelabel = ctk.CTkLabel(securityFrame, text="Please Confirm Your Identity", font=font(35))
            securityFramelabel.place(relx=0.5, rely=0.02, anchor="n")


            securitylabel = ctk.CTkLabel(securityFrame, text="Password", font=font(15))
            securitylabel.place(relx=0.34, rely=0.42, anchor="nw")

            passwordEntry = ctk.CTkEntry(securityFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
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

            settingslabel = ctk.CTkLabel(settingFrame, text="Settings", font=font(35))
            settingslabel.place(relx=0.5, rely=0.02, anchor="n")

            backButton = ctk.CTkButton(settingFrame, text="⌂", font=font(40), command= settingFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== create settings button ======================================================================================================================================================
        settingsButton = ctk.CTkButton(moreFrame, text="   Settings", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command=settings)
        settingsButton.place(relx=0, rely=.2, anchor="nw")

#=========================== create about frame ======================================================================================================================================================
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

#=========================== create about button ======================================================================================================================================================
        aboutButton = ctk.CTkButton(moreFrame, text="   About", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= about)
        aboutButton.place(relx=0, rely=.4, anchor="nw")

#=========================== create support button ======================================================================================================================================================
        supportButton = ctk.CTkButton(moreFrame, text="   Support", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0)
        supportButton.place(relx=0, rely=.6, anchor="nw")

#=========================== function to logout ======================================================================================================================================================
        def logout():
            moreFrame.place_forget()
            pickingFrame.place_forget()

#=========================== create logout button ======================================================================================================================================================
        logOutButton = ctk.CTkButton(moreFrame, text="   Log out", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", width=2000, anchor="w", height= 50, corner_radius=0, command= logout)
        logOutButton.place(relx=0, rely=.8, anchor="nw")

#=========================== algorithm to open and close more frame ======================================================================================================================================================
        if moreFrame.winfo_ismapped():
            moreFrame.place_forget()
        else:
            moreFrame.place(relx= .975, rely= .08, anchor= "ne")

#=========================== create more frame ======================================================================================================================================================
    moreFrame = ctk.CTkFrame(pickingFrame, width= 187.5, height= 250, fg_color= "#1e2121")

#=========================== create button to open up the more frame ======================================================================================================================================================
    moreButton = ctk.CTkButton(pickingFrame, text=name, font=font(18), command= more, fg_color=color, hover_color=color, width=0)
    moreButton.place(relx=.975, rely=0.05, anchor="e")
    moreButton.bind("<Enter>", on_enter)
    moreButton.bind("<Leave>", on_leave)

