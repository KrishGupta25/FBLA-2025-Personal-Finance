#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet

#Import all commands
from signUp import signUp
from error import error
from infoPage import info

#Set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#set default color
color = "#121414"
accent = "#3cb371"

#Import custom font
pyglet.font.add_file('./assets/Quicksand-Bold.ttf')

#Function to simplify font size
def font(size):
    return ("Quicksand",size)

#Creates main page or "frame" for the gui
mainFrame = ctk.CTk(fg_color = color) 
mainFrame.geometry("1200x600+180+120")

def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'





#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#=========================== ALL OF THE LOGIN PAGE STUFF ======================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================
#========================================================================================================================================================================================================================================================================


#=========================== Creating a blank page or "frame" on top of the main one to work on for the login page ======================================================================================================================================================

loginFrame = ctk.CTkFrame(mainFrame, width = 1200, height = 600, fg_color = color)
loginFrame.place(relx = 0, rely = 0)

#=========================== Creating title text that says "Login to CTE PartnerPro" ======================================================================================================================================================

loginLabel = ctk.CTkLabel(loginFrame, text="Log in to CTE PartnerPro", font=font(50))
loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#=========================== Creating a email entry box and the text above it ======================================================================================================================================================

#Text box
emailEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center")
emailEntry.place(relx= 0.5, rely= 0.45, anchor= "center")

#Text above text box
emailLabel = ctk.CTkLabel(loginFrame, text="Email", font=font(15))
emailLabel.place(relx=0.335, rely=0.36, anchor="nw")

#=========================== Creating a password entry box and the text above it ======================================================================================================================================================

#Text box
passwordEntry = ctk.CTkEntry(loginFrame, font= font(15), placeholder_text= "Password", width= 400, height= 40, justify= "center", show= "*")
passwordEntry.place(relx= 0.5, rely= 0.6, anchor= "center")

#Text above text box
passwordLabel = ctk.CTkLabel(loginFrame, text="Password", font=font(15))
passwordLabel.place(relx=0.335, rely=0.51, anchor="nw")

#============ Making sure that the email and the password is valid in our database =============================================================================================================================

def login():
    count = 0
    temp = loginInfo.find()
    for item in temp:
        if str(item['email']) == str(emailEntry.get()) and str(item['password']) == str(passwordEntry.get()):
            count +=1  
            
    if count == 1:
        loginFrame.place_forget()
    else:
        error("Wrong email or password!", loginFrame)

#=========================== Login Button ======================================================================================================================================================

loginButton = ctk.CTkButton(loginFrame, text="Log in to PartnerPro", font=font(25), command= lambda:(login()), fg_color=accent, hover_color="#63C28D", text_color= color)
loginButton.place(relx=0.5, rely=0.825, anchor="center")


#=========================== Sign in Button ======================================================================================================================================================

signupButton = ctk.CTkButton(loginFrame, text="Sign up for PartnerPro", font=font(18), command = lambda:(info(loginFrame))  lambda:(signUp(loginFrame)), fg_color=color, hover_color=color)
signupButton.place(relx=0.5, rely=0.92, anchor="center")
signupButton.bind("<Enter>", on_enter)
signupButton.bind("<Leave>", on_leave)

#=========================== Password Checkbox ======================================================================================================================================================
    
def showPasswordCommand():
    if passwordEntry.cget('show') == '':
        passwordEntry.configure(show='*')
    else:
        passwordEntry.configure(show='')

showPasswordCheckbox = ctk.CTkCheckBox(loginFrame, text="Show Password", command = showPasswordCommand)
showPasswordCheckbox.place(relx = 0.335, rely = 0.65)

#=========================== Keeps GUI Running ======================================================================================================================================================
if __name__ == "__main__":
    mainFrame.mainloop()



