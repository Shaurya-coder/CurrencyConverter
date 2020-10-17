####### Code Starts Here ########
#Step1
# Usual importing tkinter and other modules(forex-python for this project only),mainloop and defining app window default width and height,etc.
# from forex_python.converter import CurrencyRates #if you want to use forex python for rates
from tkinter import *
import requests #If you want to make a direct requests to the api for rates
import json#To convert json to dictionary in Python
root = Tk()#root is the name of the main window you caan also name it main,master,window1 etc

root.title("Currency Converter")

root.geometry('450x400')

#Step2
# Writing Title Label and other labels in window to serve as a reference to textbox.
Title_label=Label(root,text = "Currency Converter",font = 'comicsansms 30 bold',pady = 5)#.grid(row = 0,column = 1 )
Title_label.grid(row = 0,column = 1)

From_currency = Label(root,text = "From",font = 'size 15 ',pady = 5)
From_currency.grid()

To_currency = Label(root,text = "To",font = "size 15",pady = 5 )
To_currency.grid()

Amount = Label(root,text ="Amount",font = "size 15",pady = 5)
Amount.grid()
#Note:- You can not use grid and pack in the same code file.

#Step3
# Defining the type of input variable.

From_value = StringVar()
From_value.set('USD')

To_value = StringVar()
To_value.set('INR')
Amount_value = IntVar()



#Step4
# Making dropboxes for currency options.
Currencies=OptionMenu(root,From_value,
'EUR',
'GBP',
'USD',
'INR',
'AUD',
'IDR',
'BGN',
'ILS',
'ZAR',
'PHP',
'KRW',
'SEK',
'CNY',
'PLN',
'MXN',
'JPY',
'CHF',
'CZK',
'TRY',
'NOK',
'HKD',
'RUB',
'HUF',
'NZD'
)

Currencies.grid(column = 2,row = 1)


Currencies2=OptionMenu(root,To_value,
'EUR',
'GBP',
'USD',
'INR',
'AUD',
'IDR',
'BGN',
'ILS',
'ZAR',
'PHP',
'KRW',
'SEK',
'CNY',
'PLN',
'MXN',
'JPY',
'CHF',
'CZK',
'TRY',
'NOK',
'HKD',
'RUB',
'HUF',
'NZD'
)

Currencies2.grid(column = 2,row = 2)
#Step5
# Making a textbox.

From_entry = Entry(root,textvariable = From_value)
To_entry = Entry(root,textvariable = To_value)
Amount_entry = Entry(root,textvariable = Amount_value)


#Step6
# Defining the position of textbox in app window.
From_entry.grid(column = 1,row = 1 )
To_entry.grid(column = 1,row = 2)
Amount_entry.grid(column = 1,row = 3)

#Step7
# Making a function to convert the currency.
Response_label=Label(root)#Empty label 
def convert():
    global Response_label
    Response_label.destroy()
    # If you want to do through requests module.:-
    #Step I
    # Making Get requests
    r = requests.get(f"https://api.ratesapi.io/api/latest?base={From_value.get()}&symbols={To_value.get()}")
    #Step II
    # Getting the content from the page
    r = r.content
    #Step III
    # Converting Json into Python dictionary
    r = json.loads(r)
    #Step IV
    # Getting the value of rates in r
    r = r.get("rates")

    #Step V
    # Getting the value of 1 EUR(any currency) from GBP
    rates = r.get(f"{To_value.get()}")
    #Step VI
    # Multiplying the value of 1 Eur with the required quantity
    rates = rates*Amount_value.get()
    # Using Forex Python Module:-
    # c = CurrencyRates()
    # rates = c.convert(From_value.get(),To_value.get(),Amount_value.get())

    rates = float('{:.3f}'.format(rates))#To Limit the decimal places of rates to 3

    Response_label=Label(root,text = f'{rates} {To_value.get()}',font = 'comicsansms 15 bold',pady = 5)

    Response_label.grid(row = 20,column = 1)

#Step8
# Making a button and inserting the convert function into it. 

Convert_Button = Button(text = "Convert",bg = 'white',fg = 'black',font = "size 15",pady = 0,command = convert)
Convert_Button.grid(column = 1,rows = 5)

root.mainloop()

####### Code Finishes Here ########