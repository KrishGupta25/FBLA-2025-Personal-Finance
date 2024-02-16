#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
from success import success

#=========================== import all required functions ======================================================================================================================================================
from tkinter import font
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]

#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand", size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

# Custom headings
headings = ['Name', 'Type', 'Location', 'Contact Info']  # Customize these according to your requirements

def report(root, close):

    # Retrieve data from MongoDB
    data = [headings]

    # Fetch data from MongoDB collection
    for document in orgInfo.find():
        row = [document['orgName'], document['resources'], document['location'], document['contactInfo']]  # Modify according to your data structure
        data.append(row)

    # Create PDF document
    # Create PDF document
    filename = "report.pdf"
    download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')  # Get user's downloads folder
    pdf_filepath = os.path.join(download_folder, filename)
    doc = SimpleDocTemplate(pdf_filepath, pagesize=letter, topMargin=30)

    # Create a title
    styles = getSampleStyleSheet()
    title_text = "CTE Organizations"  # Customize title text
    title = Paragraph(title_text, styles['Title'])

     # Create a spacer to add space between title and table
    spacer = Spacer(1, 30)  # Adjust the height as needed
    
    # Create a table from the data
    table = Table(data)
    
    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, -1), 8),  # Set font size to 8 points
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    table.setStyle(style)

    # Build PDF document
     # Build PDF document
    elements = [title, spacer, table]  # Include title before the table
    doc.build(elements)

    close.place_forget()
    success("Successfully Created Report - PDF is in the downloads folder", root)
    