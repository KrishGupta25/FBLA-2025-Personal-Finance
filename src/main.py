#import all required dependencies
import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient
from tkextrafont import Font

#set up connections with the database
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["FBLAMain"]
login_info = db["login_info"]

root= ctk.CTk()
root.geometry("1000x500+100+100")

font = Font(file="./assets/Quicksand-Bold.ttf", family="Quicksand")

login_label = ctk.CTkLabel(root, text="login", font=(font,50))
login_label.place(relx=0.5, rely=0.2, anchor="center")


if __name__ == "__main__":
    root.mainloop()



