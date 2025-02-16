import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Set the customtkinter theme to dark
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Optional: Use a custom color theme

# Create the main window
root = ctk.CTk()
root.title("Modern Pie Chart with Dictionary in CustomTkinter")
root.geometry("600x400")
root.configure(bg="#2E2E2E")  # Dark grey background

# Data for the pie chart (using a dictionary)
data = {
    "Apples": 15,
    "Bananas": 30,
    "Cherries": 45,
    "Dates": 10
}

# Extract labels and sizes from the dictionary
labels = list(data.keys())
sizes = list(data.values())

# Modern colors for the pie chart
colors = ['#FF6F61', '#FFD166', '#06D6A0', '#118AB2']

# "Explode" the first slice (Apples)
explode = (0.1, 0, 0, 0)

# Create a Matplotlib figure and axis with a dark theme
fig, ax = plt.subplots(facecolor="#2E2E2E")  # Dark grey background for the figure
ax.set_facecolor("#2E2E2E")  # Dark grey background for the plot area

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90,
    textprops={'color': 'white'}  # White text for labels and percentages
)

# Add a legend with white text
ax.legend(wedges, labels, title="Fruits", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), labelcolor='white')

# Set the title with white text
ax.set_title("Fruit Distribution", color='white')

# Embed the Matplotlib figure in CustomTkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

# Run the application
root.mainloop()