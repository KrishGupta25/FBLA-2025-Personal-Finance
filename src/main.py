#Import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
from tkextrafont import Font


#Set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["FBLAMain"]
login_info = db["login_info"]


#Setting up the GUI
root= ctk.CTk() 
root.geometry("1000x500+100+100")


font = Font(file="./assets/Quicksand-Bold.ttf", family="Quicksand")
ctk.set_appearance_mode("Light") #I was jsut messing around, we can change it 

frame = ctk.CTkFrame(master=root)
frame.pack(pady=60,padx=60, fill="both", expand="True")

#login_label = ctk.CTkLabel(root, text="login", font=(font,50))
#login_label.place(relx=0.5, rely=0.2, anchor="center")

def login():
    print("Hello World")

login_label = ctk.CTkLabel(master = frame, text="Login", font=("Quicksand_Bold", 24))
login_label.pack(pady=20, padx=10)

username_entry = ctk.CTkEntry(master=frame, placeholder_text="username")
username_entry.pack(pady=12,padx=10)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="password", show="*")
password_entry.pack(pady=12,padx=10)

login_button = ctk.CTkButton(master=frame, text="Login",command=login)
login_button.pack(pady=12, padx=10)

RememberMe_checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me", hover_color="grey")
RememberMe_checkbox.pack(pady=12, padx=10)


if __name__ == "__main__":
    root.mainloop()



