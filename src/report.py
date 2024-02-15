#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient

#=========================== import all required functions ======================================================================================================================================================
from tkinter import font
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
orgInfo = db["orgInfo"]


def report():
    # Retrieve data from MongoDB
    data = []
    for document in orgInfo.find():
        row = [document['orgName'], document['resources'], document['location'], document['contactInfo']]  # Modify according to your data structure
        data.append(row)

    # Create PDF document
    pdf_filename = "report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    
    # Create a table from the data
    table = Table(data)
    
    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
    table.setStyle(style)

    # Build PDF document
    elements = []
    elements.append(table)
    doc.build(elements)

