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
        self.logo=Label(
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
        self.options_list = ["amazon.com", "amazon.ca", "amazon.com.au","amazon.co.uk"]
        
        #create string variable
        self.domain_opt = StringVar(self.Master)
        
        #set the default value for menu bar
        self.domain_opt.set("Select an amazon domain")
        
        #create domain selection menu bar
        question_menu = OptionMenu(self.Master, self.domain_opt, *self.options_list)
        question_menu.place(x=170,y=100)
        
        #craete a string variable
        self.url=StringVar()
        
        #create a api key lable
        self.api_label=Label(text="API Key:")
        self.api_label.place(x=50, y=134)
        
        #create api key entry for user to input
        self.api_key_entry=Entry(self.Master)
        self.api_key_entry.place(x=110, y=130)
        
        #create asin lable
        self.asin_label=Label(text="ASIN #:")
        self.asin_label.place(x=50, y=165)
        
        #create asin entry for user to input
        self.asin_entry=Entry(self.Master)
        self.asin_entry.place(x=110, y=160)
        
        #create a button
        self.Button=Button(self.Master,text="Submit",command=self.output_result)
        self.Button.place(x=300,y=200)
        
        self.warn=Label(text="",fg="red")
        self.warn.place(x=110, y=200)
        self.out1=Label(text="")
        self.out1.place(x=50, y=200)
        self.out2=Label(text="")
        self.out2.place(x=50, y=240)
        self.out3=Label(text="",font=('Arial', 20))
        self.out3.place(x=50, y=300)
        
        self.labels=[]
        for i in range(10):
            self.labels.append(Label(text=""))
            self.labels[i].place(x=50, y=330+i*20)
        
            
        #self.Master.mainloop()
        
    #get user's inputs and create url for it
    def return_url(self):
        #get value from api_key_entry
        self.api=self.api_key_entry.get()
        
        #get value from asin_entry
        self.asin=self.asin_entry.get()
        
        #get value from domain_opt in menu bar
        self.domain=self.domain_opt.get()
        
        #create url
        self.url="https://api.asindataapi.com/request?api_key="+self.api+"&type=reviews&amazon_domain="+self.domain+"&asin="+self.asin+"&review_stars=one_star&sort_by=most_helpful"
        return self.url
    def clean_content(self):
        self.out1.config(text="")
        self.out2.config(text="")
        self.out3.config(text="")
    
    def get_review(self):
        #call return url function
        self.return_url()
        
        #create a request for url
        api_request=requests.get(self.url)
        
        #convert the request to json
        to_json=json.dumps(api_request.json())
        
        #use beautiful soup to access data
        soup=BeautifulSoup(to_json)
        
        #get the text
        site_json=json.loads(soup.text)
        
        #raise exception when access failed
        if site_json['request_info']['success']==False:
            
            #API key is incorrect
            if site_json['request_info']['message']=='Supplied api_key is not valid':
                #create a label and output the error message on the window
                self.clean_content()
                self.warn=Label(text="Sorry, API key is not valid",fg="red")
                self.warn.place(x=110, y=200)
                raise Exception("API key is not valid")
                
            
            #No ASIN entered
            elif site_json['request_info']['message']=="'asin' or 'gtin' parameter must be present when 'url' is not supplied.":
                #create a label and output the error message on the window
                self.clean_content()
                self.warn.config(text="Sorry, ASIN is not valid",fg="red")
                raise Exception("Sorry, ASIN is not valid")
                
            #amazon domain is not found
            elif site_json['request_info']['message']=="'amazon_domain' parameter is invalid - for supported Amazon domains visit https://www.asindataapi.com/docs/product-data-api/reference/amazon-domains":
                #create a label and output the error message on the window
                self.clean_content()
                self.warn.config(text="Sorry, domain is not valid",fg="red")
                raise Exception("Sorry, domain is not valid")
                
                
            #ASIN is not found
            elif site_json['request_info']['http_status_code']==404:
                #create a label and output the error message on the window
                self.clean_content()
                self.warn.config(text="Sorry, ASIN is not valid",fg="red")
                raise Exception("Sorry, ASIN is not valid")
                
                
        if site_json['request_info']['success']==True:
            #raise exception when there is no bad review
            if site_json['summary']['rating_breakdown']['one_star']['count']==0:
                #create a label and output the error message on the window
                self.clean_content()
                self.warn.config(text="No bad review for this product",fg="red")
                raise Exception("No bad review for this product")
            else:
                #get all the reviews
                self.review=[i.get('body') for i in site_json['reviews'] if i.get('body')]
                #get the rating score
                self.score=site_json['summary']['rating']
                #get the one_star review count
                self.one_star_count=site_json['summary']['rating_breakdown']['one_star']['count']
                #get the one_star review percentage
                self.one_star_percentage=site_json['summary']['rating_breakdown']['one_star']['percentage']
        
        return self.review, self.score, self.one_star_count, self.one_star_percentage
