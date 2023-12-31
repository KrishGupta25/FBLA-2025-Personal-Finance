#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
import pyglet
import string

# Import all commands
from error import error

#Creates connection to database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]

#Import custom font
pyglet.font.add_file('assets/circular-std-medium-500.ttf')

#Function to simplify font size
def font(size):
    return ("circular",size)

#Setting the default color
color = "#1e1e1e"

#Instantiatation of a new page for the signup
def signUp(root):
    #Create new sign up frame over login page
    signupFrame = ctk.CTkFrame(root, width= 1200, height= 600, fg_color= color)
    signupFrame.place(relx= 0, rely= 0)

    #Creates signup to xxxx label
    loginLabel = ctk.CTkLabel(signupFrame, text="Sign up for xxxx", font=font(50))
    loginLabel.place(relx=0.5, rely=0.2, anchor="center")

#=========================== Email ======================================================================================================================================================
   
    emailLabel = ctk.CTkLabel(signupFrame, text="Email", font=font(15))
    emailLabel.place(relx=0.335, rely=0.41, anchor="nw")
    emailEntry = ctk.CTkEntry(signupFrame, font= font(15), placeholder_text= "Name@domain.com", width= 400, height= 40, justify= "center")
    emailEntry.place(relx= 0.5, rely= 0.5, anchor= "center")

#=========================== Password ======================================================================================================================================================
   
    passLabel = ctk.CTkLabel(signupFrame, text="Password", font=font(15))
    passLabel.place(relx=0.335, rely=0.61, anchor="nw")
    passEntry = ctk.CTkEntry(signupFrame, font = font(15), placeholder_text = "Password", width = 400, height= 40, justify = "center", show = "*")
    passEntry.place(relx= 0.5, rely= 0.7, anchor= "center")

#=========================== Password Checkbox ======================================================================================================================================================
    
    def showPasswordCommand():
        if passEntry.cget('show') == '':
            passEntry.configure(show='*')
        else:
            passEntry.configure(show='')

    showPasswordCheckbox = ctk.CTkCheckBox(signupFrame, text="Show Password", command = showPasswordCommand)
    showPasswordCheckbox.place(relx = 0.335, rely = 0.75)

#=========================== Checking to see a valid username and password ======================================================================================================================================================        
    
    def enter():

        #Checking password for at least one uppercase letter, one lowercase letter, one special character, and one number, and at least 8 characters
        #Checking password for "@" symbol 
        #Checking both for no spaces and making sure they arent blank

        #Getting the input from the user
        email= emailEntry.get()
        password = passEntry.get()

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
            temp = {"email": email, "password": password}
            loginInfo.insert_one(temp)
            signupFrame.place_forget()

#=========================== Sign Up Button ======================================================================================================================================================
    
    signUpButton = ctk.CTkButton(signupFrame, text="Sign up", font=font(25), command= enter, fg_color= color)
    signUpButton.place(relx=0.5, rely=0.85, anchor="center")

#=========================== Back Button ======================================================================================================================================================

    backButton = ctk.CTkButton(signupFrame, text="Back to Login Page", font=font(25), command= signupFrame.place_forget, fg_color=color)
    backButton.place(relx=0.105, rely=0.05, anchor="center")





