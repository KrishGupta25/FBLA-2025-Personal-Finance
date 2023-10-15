import tkinter as tk
import customtkinter as ctk
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["FBLAMain"]
login_info = db["login_info"]


root= ctk.CTk()
root.geometry("1000x500+100+100")


if __name__ == "__main__":
    root.mainloop()



