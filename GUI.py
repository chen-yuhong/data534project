import tkinter as tk



#create a window

window = tk.Tk()



#set the window title

window.title("APRA (Amazon Product Review Analysis)")



#set window size

window.geometry("400x600+374+182")



#create a logo

logo = tk.Label(

    text="APRA",

    font=('Arial', 30),

    fg="orange",

    bg="black",

    width=10,

    height=2

)

logo.place(x=120, y=0)



#create label for greeting

greeting = tk.Label(text="Welcome to use Amazon Product Review Analysis Tool")

greeting.place(x=40, y=70)



#api_key label

api_key_label = tk.Label(text="API Key:")

api_key_label.place(x=50, y=134)



#api_key entry

api_key = tk.Entry(window)

api_key.place(x=110, y=130)



#ASIN label

asin_label = tk.Label(text="ASIN #:")

asin_label.place(x=50, y=165)



#ASIN entry

asin = tk.Entry(window)

asin.place(x=110, y=160)



#search button

search = tk.Button(window,text="SEARCH")

search.place(x=300,y=200)

window.mainloop()
