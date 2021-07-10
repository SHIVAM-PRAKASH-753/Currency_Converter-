import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

from requests.api import request
from tkinter import messagebox


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        #if from_currency != 'USA':
        amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = converter
        self.configure(background='#99FFFF')
        self.geometry("500x300")
        self.maxsize(500, 300)
        self.minsize(500, 300)

        # Label
        self.intro_label = Label(self, text='Welcome to Currency Converter',
                                 bg='indigo', fg='yellow', relief=tk.SOLID, borderwidth=3)
        self.intro_label.config(font=('Arial', 19, 'bold'))

        self.date_label = Label(self, text=f"₹ 1 = {self.currency_converter.convert('INR','USD',1)} $ \n \n Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=55, y=5)
        self.date_label.place(x=205, y=60)
        self.frame1 = LabelFrame(self, text="Select FROM CURRENCY",
                                 padx=5, pady=5, background="#FF9933", foreground="navy blue")
        self.frame2 = LabelFrame(self, text="Select TO CURRENCY",
                                 padx=5, pady=5, background="#138808", foreground="yellow")
        self.frame3 = LabelFrame(self, text="Enter your Amount here",
                                 padx=5, pady=5, background="#CCCCCC", foreground="navy blue")
        self.frame4 = LabelFrame(self, text="Converted Amount",
                                 padx=5, pady=5, background="#CCCCCC", foreground="navy blue")

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%p')
        self.amount_field = Entry(
            self.frame3, bd=3, justify=tk.CENTER,relief=SUNKEN, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(
            self.frame4, text='',   bg='white', justify=tk.CENTER,relief=SUNKEN, width=17, borderwidth=3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("INR")  # default value

        font = ("Arial", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self.frame1, textvariable=self.from_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self.frame2, textvariable=self.to_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.pack()
        self.amount_field.pack()
        self.to_currency_dropdown.pack()
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.pack()
        self.frame1.place(x=30, y=130)
        self.frame2.place(x=340, y=130)
        self.frame3.place(x=30, y=205)
        self.frame4.place(x=340, y=205)

        # Convert button
        self.convert_button = Button(
            self, text="Get Value", fg="#000080", command=self.perform)
        self.convert_button.config(font=('Arial', 10, 'bold'))
        self.convert_button.place(x=220, y=180)

        # Exit button
        exit_button = Button(self, text="Exit", font=("Italic", 10, "bold"), command=self.quit,
                             width=8)
        exit_button.place(x=220, y=260)

    def perform(self):
        amount = float(self.amount_field.get())

        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(
            from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 5)

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = requests.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))


if __name__ == '__main__':
    url = 'http://data.fixer.io/api/latest?access_key=7adaaa4eb2b8a810b661622e746eaf40'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()
