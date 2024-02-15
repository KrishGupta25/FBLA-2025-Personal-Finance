#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
import customtkinter as ctk

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== function to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

#=========================== cunction for button highliting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'


#=========================== function for error page ======================================================================================================================================================
def success(message, root):
    newError = ctk.CTkFrame(root, width=1200, height=25, fg_color= accent, corner_radius=0)
    newError.place(relx=0, rely=0, anchor="nw")

    label = ctk.CTkLabel(newError, text=message, font=font(15), fg_color=accent, text_color="white")
    label.configure(anchor="center")
    label.place(relx=0.5, rely=0.4, anchor="center")

    newError.after(2000, newError.place_forget)