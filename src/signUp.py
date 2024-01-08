#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import os
import sys

#=========================== import all required functions ======================================================================================================================================================
from errorPage import error
from infoPage import info

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#=========================== import custom font ======================================================================================================================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

font_path = "Quicksand-bold.ttf"
pyglet.font.add_file(resource_path(font_path))

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
    

#=========================== creates new page for signing up ======================================================================================================================================================
def signUp(root):
    #Create new sign up frame over login page
    signupFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    signupFrame.place(relx= 0, rely= 0)

    #Creates signup to xxxx label
    loginLabel = ctk.CTkLabel(signupFrame, text="Sign up for xxxx", font=font(50))
    loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#=========================== Email entry box and text above entry box  ======================================================================================================================================================
   
    emailLabel = ctk.CTkLabel(signupFrame, text="Email", font=font(15))
    emailLabel.place(relx=0.335, rely=0.36, anchor="nw")
    emailEntry = ctk.CTkEntry(signupFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center")
    emailEntry.place(relx= 0.5, rely= 0.45, anchor= "center")

#=========================== Password entry box and text above entry box ======================================================================================================================================================
   
    passwordLabel = ctk.CTkLabel(signupFrame, text="Password (must include 1 uppercase letter, 1 lowercase letter, 1 special character and 1 number)", font=font(15))
    passwordLabel.place(relx=0.335, rely=0.56, anchor="nw")
    passwordEntry = ctk.CTkEntry(signupFrame, font = font(15), placeholder_text = "Password (must have at least 8 characters)", width = 400, height= 40, justify = "center", show = "*")
    passwordEntry.place(relx= 0.5, rely= 0.65, anchor= "center")

    def display(e):
        tooltipFrame.place(relx = .7, rely = 0.76, anchor = "nw")
    def hide(e):
        tooltipFrame.place_forget()

    tooltipFrame = ctk.CTkFrame(signupFrame, width= 100, height= 50, fg_color= color)
    tooltipLabel = ctk.CTkLabel(signupFrame, text="ⓘ", font=font(15))
    tooltipLabel.place(relx = 0.68, rely = 0.65, anchor = "center")

    tooltipLabel.bind("<Enter>", display)
    tooltipLabel.bind("<Leave>", hide) 

#=========================== Password Checkbox ======================================================================================================================================================
    
    def showPasswordCommand():
        if passwordEntry.cget('show') == '':
            passwordEntry.configure(show='*')
        else:
            passwordEntry.configure(show='')

    showPasswordCheckbox = ctk.CTkCheckBox(signupFrame, text="Show Password", command = showPasswordCommand, hover_color=accent, checkmark_color=accent)
    showPasswordCheckbox.place(relx = 0.335, rely = 0.7)

#=========================== Checking to see a valid username and password ======================================================================================================================================================        
    
    def enter():

        #Checking password for at least one uppercase letter, one lowercase letter, one special character, and one number, and at least 8 characters
        #Checking password for "@" symbol 
        #Checking both for no spaces and making sure they arent blank

        #Getting the input from the user
        email= emailEntry.get()
        password = passwordEntry.get()

        #Checking to see if either entry is empty
        if email == "" or password == "":
            error("Either one or more of the required fields are empty or your entry has spaces", signupFrame)

        #Checking to see if either entry has spaces
        elif email.find(" ") > -1 or password.find(" ") > -1:
            error("Either one or more of the required fields are empty or your entry has spaces", signupFrame)

        #Makeing sure there is a "@" sign in the email entry field 
        elif email.find("@") == -1:
            error("There is no '@' in your email, please try again!", signupFrame)

        #Checking to see if there is at least one uppercase character in the password
        elif any(ele.isupper() for ele in password) == False:
            error("There is no uppercase letter in your password, please try again!", signupFrame)
        
        #Checking to see if there is at least one lowercase character in the password
        elif any(ele.islower() for ele in password) == False:
            error("There is no lowercase letter in your password, please try again!", signupFrame)
       
        #Checking to see if there is at least one special character in the password
        elif (password.isalnum()) == True:
            error("There is no special characters in your password, please try again!", signupFrame)

        #Checking to see if there is at least one number in the password
        elif any(ele.isdigit() for ele in password) == False:
            error("There is no number in your password, please try again!", signupFrame)
        
        #Checking to see if there is at least 8 characters in the password
        elif len(password) <= 8:
            error("There arent 8 characters in your password, please try again!", signupFrame)

        #If all of those checks are passed then add the username and password to our database
        else:
            info(root, email, password, signupFrame)
          
    
        
#=========================== Sign Up Button ======================================================================================================================================================
    
    signUpButton = ctk.CTkButton(signupFrame, text="Next", font=font(25), command= enter, fg_color= accent, hover_color="#63C28D", text_color=color )
    signUpButton.place(relx=0.5, rely=0.8, anchor="center")

#=========================== Back Button ======================================================================================================================================================

    backButtonText = ctk.CTkLabel(signupFrame, text="Already have an account?", font=font(18), fg_color=color, text_color="#A7A7A7")
    backButtonText.place(relx=0.54, rely=0.9, anchor="e")

    backButton = ctk.CTkButton(signupFrame, text = "Log in here", font=font(18), command = signupFrame.place_forget, fg_color = color, border_width=0, width=0, hover_color=color)
    backButton.place(relx=0.54, rely=0.9, anchor="w")
    backButton.bind("<Enter>", on_enter)
    backButton.bind("<Leave>", on_leave) 

    #=========================== FOR TESTINGGGGG    ======================================================================================================================================================        
