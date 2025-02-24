#=========================== import all required packages ======================================================================================================================================================
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from pymongo import MongoClient
from PIL import ImageTk, Image
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime as dt
from projectsPage import Projects

#=========================== import all required functions ======================================================================================================================================================

from errorPage import error
from dataPage import yourData

#=========================== establish connection to database ======================================================================================================================================================
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["main"]
loginInfo = db["loginInfo"]
#=========================== import custom font ======================================================================================================================================================
class CustomTkinter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
#=========================== fucntion to simplify font size ======================================================================================================================================================
def font(size):
    return ("Quicksand",size)

#=========================== set default colors ======================================================================================================================================================
color = "#121414"
accent = "#3cb371"

#=========================== cunction for button highliting ======================================================================================================================================================
def on_enter(e):
    e.widget['foreground'] = accent

def on_leave(e):
    e.widget['foreground'] = 'white'

#=========================== funtion to create home page ======================================================================================================================================================
def pickingTransaction(root, email):

#=========================== find users preferred name and transaction details =================================================================================================================================
    temp = loginInfo.find({"email": email})
    for item in temp:
        user = item["preferredName"]
        pickingTransactionId = item["_id"]
    
    transactionInfo = db[str(pickingTransactionId)+"collection"]
    transactions = transactionInfo.find() 

#=========================== home page frame ======================================================================================================================================================
    pickingFrame = ctk.CTkFrame(root, fg_color= color)
    pickingFrame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

#=========================== no data label ======================================================================================================================================================

    noDataText = ctk.CTkLabel(pickingFrame, text="Please enter at least one piece of data \n for income and expense for statistics ", font=font(25), fg_color=color, text_color="white")
    noDataText.place_forget()
#=========================== pie chart 1 ======================================================================================================================================================
    templist = []
    
    categories = ["Entertainment", "Groceries", "Other", "Rent",  "Transportation", "Utilities" ]
    for t in transactions:
        templist.append(t)
        
    
    templist = [x for x in templist if x["resources"] != "Income"]
    templist.sort(key=lambda x: x["resources"], reverse=False)
    try:
        templist[0]
    except:
        noDataText.place(relx=0.5, rely=0.5, anchor="center")
    else:

        total_sum = 0
        for t in templist:
            total_sum += t["amount"]
        
        category_sums = []
        for c in categories:
            temp_sum = 0
            check = 0
            for t in templist:
                if t["resources"] == c:
                    check += 1
                    temp_sum += t["amount"]
            category_sums.append(temp_sum)
        
        data = {
        categories[0]: (category_sums[0]/total_sum)*100,
        categories[1]: (category_sums[1]/total_sum)*100,
        categories[2]: (category_sums[2]/total_sum)*100,
        categories[3]: (category_sums[3]/total_sum)*100,
        categories[4]: (category_sums[4]/total_sum)*100,
        categories[5]: (category_sums[5]/total_sum)*100
        }

        colors = ['#FF6F61', '#FFD166', '#06D6A0', '#118AB2', '#A78BFA', '#FF9F85', '#2EC4B6']

        # Create a Matplotlib figure and axis with a dark theme
        fig, ax = plt.subplots(facecolor= color)  # Dark grey background for the figure
        ax.set_facecolor(color)  # Dark grey background for the plot area
        
        

        # Create the pie chart
        wedges, texts, idk1 = ax.pie(
            list(data.values()),
            colors=colors,
            autopct= '%1.1f%%',
            shadow=True,
            startangle=90,
            textprops={'fontsize': 10,  # Font size
            'fontweight': 'bold',  # Font weight
            'fontfamily': "Quicksand",  # Font family
            'color': 'white'  # Font color}  # White text for labels and percentages
            }
        )

        # Add a legend with white text
        ax.legend(wedges, categories, loc="center left", bbox_to_anchor=(.9, 0, 0.5, 1), 
            prop={
            'size': 10,  # Font size
            'weight': 'bold',  # Font weight
            'family': 'Quicksand'  # Font family
            },
            labelcolor='white',
            facecolor= color,
            edgecolor= color,
            )

        # Set the title with white text
        ax.set_title("All Expenses", color='white', 
        fontdict={
        'fontsize': 10,
        'fontweight': 'bold',
        'fontfamily': 'Quicksand',
        'color': 'white'
        })

        # Embed the Matplotlib figure in CustomTkinter
        canvas = FigureCanvasTkAgg(fig, master=pickingFrame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.25, rely=0.32, relwidth= .6, relheight= .6, anchor="center")


#=========================== pie chart 2 ======================================================================================================================================================templist = []
        
        categories1 = ["Income", "Expenses" ]
        templist = []
        transactions = transactionInfo.find()

        for t in transactions:
            templist.append(t)

        expense_sum = 0
        income_sum = 0
        for x in templist:
            if x["resources"] != "Income":
                expense_sum += x["amount"]
            else:
                income_sum += x["amount"]

        total_sum = 0
        for t in templist:
            total_sum += t["amount"]
        
        colors = ['#FF9F85', '#2EC4B6']

        # Create a Matplotlib figure and axis with a dark theme
        fig1, ax1 = plt.subplots(facecolor= color)  # Dark grey background for the figure
        ax1.set_facecolor(color)  # Dark grey background for the plot area
        
        fig1.set_figwidth(pickingFrame.winfo_width()*6)
        fig1.set_figheight(pickingFrame.winfo_height()*4)

        # Create the pie chart
        wedges1, texts, idk2 = ax1.pie(
            [(income_sum/total_sum)*100, (expense_sum/total_sum)*100],
            colors=colors,
            autopct= '%1.1f%%',
            shadow=True,
            startangle=90,
            textprops={'fontsize': 10,  # Font size
            'fontweight': 'bold',  # Font weight
            'fontfamily': "Quicksand",  # Font family
            'color': 'white'  # Font color}  # White text for labels and percentages
            }
        )

        # Add a legend with white text
        ax1.legend(wedges1, categories1, loc="center left", bbox_to_anchor=(.9, 0, 0.5, 1), 
            prop={
            'size': 10,  # Font size
            'weight': 'bold',  # Font weight
            'family': 'Quicksand'  # Font family
            },
            labelcolor='white',
            facecolor= color,
            edgecolor= color,
            )

        # Set the title with white text
        ax1.set_title("Total spending", color='white', 
        fontdict={
        'fontsize': 10,
        'fontweight': 'bold',
        'fontfamily': 'Quicksand',
        'color': 'white'
        })

        # Embed the Matplotlib figure in CustomTkinter
        canvas1 = FigureCanvasTkAgg(fig1, master=pickingFrame)
        canvas1.draw()
        canvas1.get_tk_widget().place(relx=0.75, rely=0.32, relwidth= .6, relheight= .6, anchor="center") 

#=========================== create line graph  ======================================================================================================================================================       
    
    plt.rcParams["font.family"] = "Quicksand"  
    plt.rcParams["font.size"] = 10
    
    transactions = transactionInfo.find()
    transaction_dates = []
    for t in transactions:
        transaction_dates.append(t)
    
    sorted_data = sorted(transaction_dates, key=lambda x: dt.strptime(x["Date"], "%m/%d/%Y"))

    # Assign numerical values based on chronological order
    for index, item in enumerate(sorted_data, start=1):
        item["time_num"] = index
    
    sorted_total = 0
    sorted_total_list = []
    dates = [dt.strptime(item["Date"], "%m/%d/%Y") for item in sorted_data]
    for data in sorted_data:
        if data["resources"] == "Income":
            sorted_total += data["amount"]
        else:
            sorted_total -= data["amount"]
        sorted_total_list.append(sorted_total)
        
    balances = [item for item in sorted_total_list]

# Create the line graph
    fig2, ax2 = plt.subplots()  # Create a figure and axis
    ax2.plot(dates, balances, marker='o', linestyle='-', label="Balance Over Time", color = accent)
        
    ax2.set_title("Change in Balance Over Time", color = 'white',)
    ax2.grid(True)
    fig2.autofmt_xdate()
    canvas2 = FigureCanvasTkAgg(fig2, master=pickingFrame)
    canvas2.draw()
    canvas2.get_tk_widget().place(relx= 0.035, rely= 0.8, relwidth= 1.05, relheight= .55, anchor= "w")
    fig2.patch.set_facecolor(color) 
    ax2.set_facecolor(color)
    ax2.set_xticks([])
    ax2.set_xticklabels([])
    ax2.tick_params(axis='y', colors='white')
    for spine in ax2.spines.values():
        spine.set_color(color)


#=========================== welcomes user to home page ======================================================================================================================================================
    labelText = ctk.CTkLabel(pickingFrame, text="Hello, " + user, font=font(25), fg_color=color, text_color="white")
    labelText.place(relx=0.55, rely=0.05, anchor="center")
    
    
#=========================== side frame ======================================================================================================================================================
    sideFrame = ctk.CTkFrame(root, fg_color= "#0f1010")
    sideFrame.place(relx= 0, rely= 0, relwidth= 1/8, relheight= 1, anchor= "nw")

#=========================== create Home button ======================================================================================================================================================

    homeButton = ctk.CTkButton(sideFrame, text="  ⌂ Home", font=font(18), fg_color= "#0f1010", hover_color="#2a2e2e", width=150, anchor="w", height= 50, corner_radius=0, command= lambda: [pickingFrame.place_forget(), pickingTransaction(root, email)])
    homeButton.place(relx=0, rely=0, anchor="nw")

#=========================== create Home button ======================================================================================================================================================

    tableButton = ctk.CTkButton(sideFrame, text="  📖 Your Data", font=font(18), fg_color= "#0f1010", hover_color="#2a2e2e", width=150, anchor="w", height= 50, corner_radius=0, command= lambda: [yourData(pickingFrame ,email)])
    tableButton.place(relx=0, rely=0.083, anchor="nw")

#=========================== create Projects Button ======================================================================================================================================================
    projectsButton = ctk.CTkButton(sideFrame, text="  📂 Projects", font=font(18), fg_color= "#0f1010", hover_color="#2a2e2e", width=150, anchor="w", height= 50, corner_radius=0, command= lambda: [Projects(pickingFrame ,email)])
    projectsButton.place(relx=0, rely=0.166, anchor="nw")

#=========================== find users first and last name ======================================================================================================================================================
    temp = loginInfo.find({"email": email})
    for item in temp:
        first = item["firstName"]
        last = item["lastName"]
        name = f'{first} {last}'

#=========================== create pop up window for more options ======================================================================================================================================================
    def more():
        def account():
            moreFrame.place_forget()

#=========================== get all user data ======================================================================================================================================================
            temp = loginInfo.find({"email": email})
            for item in temp:
                first = item["firstName"]
                last = item["lastName"]
                preferred = item["preferredName"]
                password = item["password"]
                
#=========================== create account frame ======================================================================================================================================================
            accountFrame = ctk.CTkFrame(root, fg_color= color, bg_color= color)
            accountFrame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1, anchor= "nw")

            accountlabel = ctk.CTkLabel(accountFrame, text="Acount Details", font=font(35), fg_color=color, text_color="white")
            accountlabel.place(relx=0.5, rely=0.02, anchor="n")

#=========================== password entry ======================================================================================================================================================
            passwordLabel2 = ctk.CTkLabel(accountFrame, text="Password", font=font(15), fg_color=color, text_color="white")
            passwordLabel2.place(relx=0.335, rely=0.16, anchor="nw")
            
            passwordEntry2 = ctk.CTkEntry(accountFrame, font= font(15), justify= "center", fg_color=color, text_color="white")
            passwordEntry2.place(relx= 0.5, rely= 0.25, relwidth= 1/3, relheight= 1/15, anchor= "center")
            passwordEntry2.insert(0, password)
            passwordEntry2.bind('<FocusIn>', lambda x: passwordEntry2.select_range(0, "end"))

#=========================== first name entry ======================================================================================================================================================
            firstNameLabel = ctk.CTkLabel(accountFrame, text="First Name", font=font(15), fg_color=color, text_color="white")
            firstNameLabel.place(relx=0.335, rely=0.33, anchor="nw")
            
            firstNameEntry = ctk.CTkEntry(accountFrame, font= font(15), justify= "center", fg_color=color, text_color="white")
            firstNameEntry.place(relx= 0.5, rely= 0.42, relwidth= 1/3, relheight= 1/15, anchor= "center")
            firstNameEntry.insert(0, first)
            firstNameEntry.bind('<FocusIn>', lambda x: firstNameEntry.select_range(0, "end"))

#=========================== last name entry ======================================================================================================================================================
            lastNameLabel = ctk.CTkLabel(accountFrame, text="Last Name", font=font(15), fg_color=color, text_color="white")
            lastNameLabel.place(relx=0.335, rely=0.5, anchor="nw")
            
            lastNameEntry = ctk.CTkEntry(accountFrame, font= font(15), justify= "center", fg_color=color, text_color="white")
            lastNameEntry.place(relx= 0.5, rely= 0.59, relwidth= 1/3, relheight= 1/15, anchor= "center")
            lastNameEntry.insert(0, last)
            lastNameEntry.bind('<FocusIn>', lambda x: lastNameEntry.select_range(0, "end"))

#=========================== preferred name entry ======================================================================================================================================================
            preferredNameLabel = ctk.CTkLabel(accountFrame, text="Preferred Name", font=font(15), fg_color=color, text_color="white")
            preferredNameLabel.place(relx=0.335, rely=0.67, anchor="nw")
            
            preferredNameEntry = ctk.CTkEntry(accountFrame, font= font(15), justify= "center", fg_color=color, text_color="white")
            preferredNameEntry.place(relx= 0.5, rely= 0.76, relwidth= 1/3, relheight= 1/15, anchor= "center")
            preferredNameEntry.insert(0, preferred)
            preferredNameEntry.bind('<FocusIn>', lambda x: preferredNameEntry.select_range(0, "end"))

            backButton = ctk.CTkButton(accountFrame, text="⌂", font=font(40), command= accountFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== password check ======================================================================================================================================================
            def confirm():
                #Checking to see if either entry is empty
                if passwordEntry2.get() == "":
                    error("Either One Or More Of The Required Fields Are Empty Or Your Entry Has Spaces", accountFrame)

                #Checking to see if either entry has spaces
                elif passwordEntry2.get().find(" ") > -1:
                    error("Either One Or More Of The Required Fields Are Empty Or Your Entry Has Spaces", accountFrame)

                #Checking to see if there is at least one uppercase character in the password
                elif any(ele.isupper() for ele in passwordEntry2.get()) == False:
                    error("There Is No Uppercase Letter In Your Password, Please Try Again!", accountFrame)
                
                #Checking to see if there is at least one lowercase character in the password
                elif any(ele.islower() for ele in passwordEntry2.get()) == False:
                    error("There Is No Lowercase Letter In Your Password, Please Try Again!", accountFrame)
            
                #Checking to see if there is at least one special character in the password
                elif (passwordEntry2.get().isalnum()) == True:
                    error("There Are No Special Characters In Your Password, Please Try Again!", accountFrame)

                #Checking to see if there is at least one number in the password
                elif any(ele.isdigit() for ele in passwordEntry2.get()) == False:
                    error("There Is No Number In Your Password, Please Try Again!", accountFrame)
                
                #Checking to see if there is at least 8 characters in the password
                elif len(passwordEntry2.get()) <= 8:
                    error("There Arent 8 Characters In Your Password, Please Try Again!", accountFrame)

                #If all of those checks are passed then replace all the changed values
                else:
                    loginInfo.replace_one({"email": email}, {"email": email, "password": passwordEntry2.get(), "firstName": firstNameEntry.get(), "lastName": lastNameEntry.get(), "preferredName": preferredNameEntry.get()})
                    confirmLabel = ctk.CTkLabel(accountFrame, text="*all changes have been saved, please log out for changes to take effect", font=font(15), text_color=accent, fg_color=color)
                    confirmLabel.place(relx=0.5, rely=.83, anchor="center")
                


            confirmButton = ctk.CTkButton(accountFrame, text="Confirm", font=font(25), command = confirm, fg_color=color, hover_color=color)
            confirmButton.place(relx=0.5, rely=0.9, anchor="center")
            confirmButton.bind("<Enter>", on_enter)
            confirmButton.bind("<Leave>", on_leave)

#=========================== create security frame over account frame ======================================================================================================================================================
            securityFrame = ctk.CTkFrame(accountFrame, fg_color= color, bg_color= color)
            securityFrame.place(relx= 0, rely= 0, relwidth= 1, relheight= 1, anchor= "nw")

            back1Button = ctk.CTkButton(securityFrame, text="⌂", font=font(40), command= lambda: [securityFrame.place_forget(), accountFrame.place_forget()], fg_color=color, hover_color=color, width=0, height=0)
            back1Button.place(relx=.02, rely=0.001, anchor="nw")
            back1Button.bind("<Enter>", on_enter)
            back1Button.bind("<Leave>", on_leave)

            securityFramelabel = ctk.CTkLabel(securityFrame, text="Please Confirm Your Identity", font=font(35), fg_color=color, text_color="white")
            securityFramelabel.place(relx=0.5, rely=0.02, anchor="n")


            securitylabel = ctk.CTkLabel(securityFrame, text="Password", font=font(15), fg_color=color, text_color="white")
            securitylabel.place(relx=0.34, rely=0.42, anchor="nw")

            passwordEntry = ctk.CTkEntry(securityFrame, font= font(15), placeholder_text= "Password", justify= "center", show= "*", fg_color=color, text_color="white")
            passwordEntry.place(relx= 0.5, rely= 0.5, relwidth= 1/3, relheight= 1/15, anchor= "center")

#=========================== function for submittion ======================================================================================================================================================
            def submit():
                entry = passwordEntry.get()
                values = loginInfo.find({'email': email})
                for x in values:
                    if x['password'] == entry:
                        securityFrame.place_forget()
                    else:
                        error("Incorrect Password Please Try Again", securityFrame)

#=========================== create submittion button ======================================================================================================================================================
            submitButton = ctk.CTkButton(securityFrame, text="Submit", font=font(18), command = submit, fg_color=color, hover_color=color)
            submitButton.place(relx=0.5, rely=0.6, anchor="center")
            submitButton.bind("<Enter>", on_enter)
            submitButton.bind("<Leave>", on_leave)


#=========================== create account button ======================================================================================================================================================
        accountButton = ctk.CTkButton(moreFrame, text="   Account", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", anchor="w", corner_radius=0, command = account)
        accountButton.place(relx=0, rely=0, relwidth= 1, relheight= 1/3, anchor="nw")

#=========================== create about frame ======================================================================================================================================================
        def about():
            moreFrame.place_forget()
            aboutFrame = ctk.CTkFrame(pickingFrame, width=1200, height=600, fg_color= color, bg_color= color)
            aboutFrame.place(relx= 0, rely= 0, anchor= "nw")

            AboutUslabel = ctk.CTkLabel(aboutFrame, text="About Us ", font=font(35), fg_color=color, text_color="white")
            AboutUslabel.place(relx=0.5, rely=0.02, anchor="n")

            AboutUstext = ctk.CTkLabel(aboutFrame, text="""Welcome to our Future Business Leaders of America (FBLA) Programming and Coding project for 2024-2025! We, Harishankar Rajesh and
            \nKrish Gupta, are seniors at River Ridge Highschool and have spent three months developing a busniness/transaction storage platform with a  
            \nOur system is designed to be able to easily add, store, view, edit, remove, seach, and filter businesses while also implementing a 
            \nfriendly and effecient UI. This project involved in-depth learning of various software development facets, while also enhancing our
            \nability to devise effective solutions to complex problems. The journey was challenging but rewarding, with the final product serving as 
            \nboth a tool for fostering a more interactive educational environment and a testament to our journey into the world of programming. 
            \nfireplaypus375@gmail.com (Haris Rajesh) 
            \nkrishgupta2025@gmail.com(Krish Gupta) """
            , font=font(17), fg_color=color, text_color="white")
            AboutUstext.place(relx=0.5, rely=0.55, anchor="center")

            backButton = ctk.CTkButton(aboutFrame, text="⌂", font=font(40), command= aboutFrame.place_forget, fg_color=color, hover_color=color, width=0, height=0)
            backButton.place(relx=.02, rely=0.001, anchor="nw")
            backButton.bind("<Enter>", on_enter)
            backButton.bind("<Leave>", on_leave)

#=========================== create about button ======================================================================================================================================================
        aboutButton = ctk.CTkButton(moreFrame, text="   About", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", anchor="w", corner_radius=0, command= about)
        aboutButton.place(relx=0, rely=.33, relwidth= 1, relheight= 1/3, anchor="nw")

#=========================== function to logout ======================================================================================================================================================
        def logout():
            moreFrame.place_forget()
            pickingFrame.place_forget()

#=========================== create logout button ======================================================================================================================================================
        logOutButton = ctk.CTkButton(moreFrame, text="   Log out", font=font(15), fg_color= "#1e2121", hover_color="#2a2e2e", anchor="w", corner_radius=0, command= logout)
        logOutButton.place(relx=0, rely=.66, relwidth= 1, relheight= 1/3, anchor="nw")

#=========================== algorithm to open and close more frame ======================================================================================================================================================
        if moreFrame.winfo_ismapped():
            moreFrame.place_forget()
        else:
            moreFrame.place(relx= .975, rely= .08, relwidth= 5/32, relheight= 1/4, anchor= "ne")

#=========================== create more frame ======================================================================================================================================================
    moreFrame = ctk.CTkFrame(pickingFrame, fg_color= "#1e2121")

#=========================== create button to open up the more frame ======================================================================================================================================================
    moreButton = ctk.CTkButton(pickingFrame, text="⚙", font=font(25), command= more, fg_color=color, hover_color=color, width=0)
    moreButton.place(relx=.975, rely=0.06, anchor="e")
    moreButton.bind("<Enter>", on_enter)
    moreButton.bind("<Leave>", on_leave)
