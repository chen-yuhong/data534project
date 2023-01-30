from tkinter import *
import requests
from bs4 import BeautifulSoup
import json
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class APRA():
    #initialize
    def __init__(self):
        #create a window
        self.Master=Tk()
        
        #set title
        self.Master.title("APRA (Amazon Product Review Analysis)")
        
        #set window size
        self.Master.geometry("400x600+374+182")
        
        #create a logo
        self.Label=Label(
           text="APRA",
           font=('Arial', 30),
           fg="orange",
           bg="black",
           width=10,
           height=2
           ).place(x=120, y=0)
        
        #create a greeting
        self.Label=Label(
           text="Welcome to use Amazon Product Review Analysis Tool"
           ).place(x=40, y=70)
        
        #create a amazon domain lable
        self.domain_label=Label(text="Amazon Domain:").place(x=50, y=100)
        
        #option list for menu bar
        options_list = ["amazon.com", "amazon.ca", "amazon.com.au","amazon.co.uk"]
        
        #create string variable
        self.domain_opt = StringVar(self.Master)
        
        #set the default value for menu bar
        self.domain_opt.set("Select an amazon domain")
        
        #create domain selection menu bar
        question_menu = OptionMenu(self.Master, self.domain_opt, *options_list)
        question_menu.place(x=170,y=100)
        
        #craete a string variable
        self.url=StringVar()
        
        #create a api key lable
        self.api_label=Label(text="API Key:").place(x=50, y=134)
        
        #create api key entry for user to input
        self.api_key_entry=Entry(self.Master)
        self.api_key_entry.place(x=110, y=130)
        
        #create asin lable
        self.asin_label=Label(text="ASIN #:").place(x=50, y=165)
        
        #create asin entry for user to input
        self.asin_entry=Entry(self.Master)
        self.asin_entry.place(x=110, y=160)
        
        #create a button
        self.Button=Button(self.Master,text="Submit",command=self.output_result)
        self.Button.place(x=300,y=200)
        
        self.Master.mainloop()
