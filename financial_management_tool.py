from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime


class DataUnavailableError(Exception):
    pass

class MoneyManagement:
    """A class to manage income and expenses. Income and expenses work on a key:val pair of Month:value"""

    def __init__(self):
        self.income = {}
        self.expenses = {}

    def change_income(self, value: str) -> None:
        """Change the monthly income for the current month.

        Args:
            value (str): The new income value.

        """

        income = float(value)
        currMonth = datetime.now().month
        self.income[currMonth] = income
     
    def adjust_expenses(self, value: str) -> None:
        """Adjust the monthly expenses for the current month.

        Args:
            value (str): The new expenses value.

        """

        expenses = float(value)
        currMonth = datetime.now().month

        self.expenses[currMonth] = expenses

    def get_monthly_expenses(self, value: str) -> None:
        """Get the monthly expenses for the current month.

        Returns:
            float: The monthly expenses.

        """
        curr_month = datetime.now().month
        if curr_month in self.expenses:
            return self.expenses[curr_month]
        else:
            raise DataUnavailableError("Monthly expenses data is not available for this month")

    def get_monthly_income(self) -> float:
        """Get the monthly income for the current month.

        Returns:
            float: The monthly income.

        """

        curr_month = datetime.now().month
        if curr_month in self.income:
            return self.income[curr_month]
        else:
            raise DataUnavailableError("Monthly income data is not available for this month")
    
    def get_yearly_income(self) -> float:
        """Get the total income for the current year.

        Returns:
            float: The total income for the current year.

        """
        total_income = 0.0
        for month in self.income:
            total_income += self.income[month]
        return total_income
    
    def get_yearly_expenses(self) -> float:
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

        self.yearly_income_goal = 0.0 # Can be adjusted to handle multiple years
        self.yearly_expense_goal = 0.0

    def _get_month_num(self, month_name: str) -> int:
        """Private helper method, converts month name to its corresponding number.

        Args:
            month_name (str): The name of the month.

        Returns:
            int: The number representing the month.

        """
        months = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        return months.get(month_name.capitalize())

    def update_monthly_goal(self, goal: str, type: str, month: str = None) -> None:
        """Update the monthly income goal for the current month.

        Args:
            goal (str): The new monthly income goal.
            type (str): Specifies whether income[i] or expense[e]
            month (str, optional): Specifies the month to update the goal for (e.g., 'January', 'February', etc.).
                If not provided, the current month is used.

        """

        currMonth = datetime.now().month
        if month:
            month_num = self._get_month_number(month)
            if month_num is None:
                raise DataUnavailableError("Invalid month name")
        else:
            month_num = currMonth
        if type == "i":
            self.income_goal[month_num] = float(goal)
        else:
            self.expense_goal[month_num] = float(goal)
    

    def get_monthly_goal(self, type: str) -> float:
        """Get the monthly income goal for the current month.
        Args:
            type (str): Specifies whether income[i] or expense[e]

        Returns:
            float: The monthly income goal.

        """

        currMonth = datetime.now().month
        if type.lower() == "i":
            return self.income_goal[currMonth]
        else:
            return self.expense_goal[currMonth]
    
    def update_yearly_income_goal(self, goal: str) -> None:
        """Update the yearly income goal.

        Args:
            goal (str): The new yearly income goal.
            type (str): Specifies whether income[i] or expense[e]

        """
        self.yearly_income_goal = float(goal)
    
    def get_yearly_income_goal(self) -> float:
        """Get the yearly income goal.

        Returns:
            float: The yearly income goal.

        """
        return self.yearly_income_goal
    

    def get_monthly_expense_goal(self) -> float:
        """Get the monthly expense goal for the current month.

        Returns:
            float: The monthly expense goal.

        """
        return self.income_goal[datetime.now().month]
    
    def update_yearly_expense_goal(self, goal: str) -> None:
        """Update the yearly expense goal.

        Args:
            goal (str): The new yearly expense goal.

        """
        self.yearly_expense_goal = float(goal)

    def get_yearly_expense_goal(self) -> float:
        """Get the yearly expense goal.

        Returns:
            float: The yearly expense goal.

        """
        return self.yearly_expense_goal

class GUI_management:
    def __init__(self):
        self.window = Tk()
        self.window.title("Financial Management Tool")

        self.money_management = MoneyManagement()
        self.goals = Goals()

    def content_frame(self):
        self.mainframe = ttk.Frame(self.window, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def plugin_creation(self):
        self.income_var = StringVar()

        income_label = Label(self.window, text="Income:")
        income_label.pack()

        income_entry = ttk.Entry(self.window, widget=7, textvariable=self.income_var)
        income_entry.pack()

        income_button = Button(self.window, text="Update Income", command=lambda: self.update_income(self.income_var.get()))
        income_button.pack()
    
    def update_income(self, income_value):
        self.money_management.change_income(income_value)

    def update_expense(self):
        expense_value = self.expense_var.get()

    def start(self):
        self.window.mainloop()

def main():
    """ Main program """
    gui = GUI_management()
    gui.content_frame()
    gui.plugin_creation()
    gui.start()

    return 0

if __name__ == "__main__":
    main()
