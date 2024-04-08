from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime


class MoneyManagement:

    def __init__(self):
        self.income = {}
        self.expenses = {}
    """Income and expenses work on a key:val pair of Month:value"""
    def change_income(self, value):
        income = int(value)
        currMonth = datetime.now().month
        #If there is a previous monthly[incase add/subtract better than overwrite]
        """ if self.income[currMonth]:
            monthlyIncome = self.income[currMonth]
            adjustedIncome = monthlyIncome + income
            self.income[currMonth] = adjustedIncome
        else: """
        self.income[currMonth] = income
    
    def get_income(self):
        return self.income[datetime.now().month]
    
    def adjust_expenses(self, value):
        expenses = int(value)
        currMonth = datetime.now().month

        self.expenses[currMonth] = expenses


window = Tk()
window.title("Finance Manager")

income = {}
expenses = {}
goals = {}

fig = Figure(figsize=(6, 4))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

def add_income():
    amount = float(income_entry.get())
    income["Salary"] = amount
    update_income_display()

def update_income_display():
    return

window.mainloop()
