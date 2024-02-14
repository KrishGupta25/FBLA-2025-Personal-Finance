 
# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label
my_label = HTMLLabel(root, html="https://www.google.com/maps/dir/28.2704324,-82.6306974/E%C5%8DS+Fitness,+17634+Harpers+Run,+Lutz,+FL+33558/@28.2360383,-82.6187884,13z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x88c2bdb94f14d48b:0xc273f0d1cc6a0ac4!2m2!1d-82.5244523!2d28.1923397!3e0?entry=ttu")
 
# Adjust label
my_label.pack(pady=20, padx=20)
 
# Execute Tkinter
root.mainloop()