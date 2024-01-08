import tkinter as tk

class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Specify the custom font family name
        custom_font_family = "Quicksand"

        # Use the custom font in a Label widget
        label = tk.Label(self, text="Hello, Custom Font!", font=(custom_font_family, 12))
        label.pack()

if __name__ == "__main__":
    app = CustomTkinter()
    app.mainloop()



  