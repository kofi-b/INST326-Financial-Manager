from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime

"""May separate classes into standalone files for readability"""

class MoneyManagement:
    """A class to manage income and expenses. Income and expenses work on a key:val pair of Month:value"""

    def __init__(self):
        self.income = {}
        self.expenses = {}
    def change_income(self, value):
        """Change the monthly income for the current month.

        Args:
            value (float): The new income value.

        """
        income = float(value)
        currMonth = datetime.now().month
        #If there is a previous monthly[incase add/subtract better than overwrite]
        """ if self.income[currMonth]:
            monthlyIncome = self.income[currMonth]
            adjustedIncome = monthlyIncome + income
            self.income[currMonth] = adjustedIncome
        else: """
        self.income[currMonth] = income
     
    def adjust_expenses(self, value):
        """Adjust the monthly expenses for the current month.

        Args:
            value (float): The new expenses value.

        """
        expenses = float(value)
        currMonth = datetime.now().month

        self.expenses[currMonth] = expenses

    def get_monthly_expenses(self):
        """Get the monthly expenses for the current month.

        Returns:
            float: The monthly expenses.

        """
        return self.expenses[datetime.now().month]

    def get_monthly_income(self):
        """Get the monthly income for the current month.

        Returns:
            float: The monthly income.

        """
        return self.income[datetime.now().month]
    
    def get_yearly_income(self):
        """Get the total income for the current year.

        Returns:
            float: The total income for the current year.

        """
        total_income = 0.0
        for month in self.income:
            total_income += self.income[month]
        return total_income
    
    def get_yearly_expenses(self):
        """Get the total expenses for the current year.

        Returns:
            float: The total expenses for the current year.

        """
        total_expenses = 0.0
        for month in self.expenses:
            total_expenses += self.expenses[month]
        return total_expenses
    
class Goals:
    """A class to manage financial goals."""

    def __init__(self):
        """Initialize empty dictionaries and yearly goals."""
        self.expense_goal = {} # Add button to allow setting a reduction in expenses
        self.income_goal = {}

        self.yearly_income_goal = 0 # Can be adjusted to handle multiple years
        self.yearly_expense_goal = 0

    
    def update_monthly_income_goal(self, goal):
        """Update the monthly income goal for the current month.

        Args:
            goal (float): The new monthly income goal.

        """
        currMonth = datetime.now().month
        self.income_goal[currMonth] = float(goal)

    def get_monthly_income_goal(self):
        """Get the monthly income goal for the current month.

        Returns:
            float: The monthly income goal.

        """
        return self.income_goal[datetime.now().month]
    
    def update_yearly_income_goal(self, goal):
        """Update the yearly income goal.

        Args:
            goal (float): The new yearly income goal.

        """
        self.yearly_income_goal = float(goal)
    
    def get_yearly_income_goal(self):
        """Get the yearly income goal.

        Returns:
            float: The yearly income goal.

        """
        return self.yearly_income_goal
    
    def update_monthly_expense_goal(self, goal):
        """Update the monthly expense goal for the current month.

        Args:
            goal (float): The new monthly expense goal.

        """
        currMonth = datetime.now().month
        self.expense_goal[currMonth] = float(goal)

    def get_monthly_expense_goal(self):
        """Get the monthly expense goal for the current month.

        Returns:
            float: The monthly expense goal.

        """
        return self.income_goal[datetime.now().month]
    
    def update_yearly_expense_goal(self, goal):
        """Update the yearly expense goal.

        Args:
            goal (float): The new yearly expense goal.

        """
        self.yearly_expense_goal = float(goal)

    def get_yearly_expense_goal(self):
        """Get the yearly expense goal.

        Returns:
            float: The yearly expense goal.

        """
        return self.yearly_expense_goal


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
