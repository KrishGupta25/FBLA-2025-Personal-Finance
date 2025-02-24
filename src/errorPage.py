#=========================== import all requ accentpackages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk

#=========================== set default colors ======================================================================================================================================================
accent = "#D2042D"

#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== function to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)


#=========================== function for error page ======================================================================================================================================================
def error(message, root):

    newError = ctk.CTkFrame(root, fg_color= accent,corner_radius=0)
    newError.place(relx=0, rely=0, relwidth= 1, relheight= 1/24, anchor="nw")

    label = ctk.CTkLabel(newError, text=message, font=font(15), fg_color= accent, text_color="white")
    label.configure(anchor="center")
    label.place(relx=0.5, rely=0.4, anchor="center")

    newError.after(4000, newError.place_forget)
    


    