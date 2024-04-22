from tkinter import *
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 

class DataUnavailableError(Exception):
    def __init__(self, message="Data is unavailable"):
        self.message = message
        super().__init__(self.message)

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
    def __init__(self, money_management, goals):
        self.window = Tk()
        self.window.title("Financial Management Tool")

        self.money_management = money_management
        self.goals = goals

    def content_frame(self):
        self.mainframe = ttk.Frame(self.window, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def income_widgets(self):
        income_label = Label(self.mainframe, text="Income:")
        income_label.grid(column=0, row=0, sticky=W)

        self.income_var = StringVar()
        income_entry = ttk.Entry(self.mainframe, textvariable=self.income_var)
        income_entry.grid(column=1, row=0, sticky=(W,E))

        income_button = Button(self.mainframe, text="Update Income", command=self.update_income)
        income_button.grid(column=2, row=0, sticky=W)

    def update_income(self):
        income_value = self.income_var.get()
        self.money_management.change_income(income_value)

    def expenses_widgets(self):
        expenses_label = Label(self.mainframe, text="Expenses:")
        expenses_label.grid(column=0, row=1, sticky=W)

        self.expenses_var = StringVar()
        expenses_entry = ttk.Entry(self.mainframe, textvariable=self.expenses_var)
        expenses_entry.grid(column=1, row=1, sticky=(W,E))

        expenses_button = Button(self.mainframe, text="Update Expenses", command=self.update_expenses)
        expenses_button.grid(column=2, row=1, sticky=W)

    def update_expenses(self):
        expenses_value = self.expenses_var.get()
        self.money_management.adjust_expenses(expenses_value)

    def goals_widgets(self):
        goals_label = Label(self.mainframe, text="Monthly Income Goal:")
        goals_label.grid(column=0, row=2, sticky=W)

        self.goals_var = StringVar()
        goals_entry = ttk.Entry(self.mainframe, textvariable=self.goals_var)
        goals_entry.grid(column=1, row=2, sticky=(W,E))

        goals_button = Button(self.mainframe, text="Set Goal", command=self.set_goal)
        goals_button.grid(column=2, row=2, sticky=W)

    def set_goal(self):
        goal_value = self.goals_var.get()
        self.goals.update_monthly_goal(goal_value, 'i')

    def plot_chart(self):
        # Get monthly income and expenses data
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        income_data = [self.money_management.income.get(month, 0) for month in range(1, 13)]
        expenses_data = [self.money_management.expenses.get(month, 0) for month in range(1, 13)]

        # Create a bar chart
        fig, ax = plt.subplots()
        bar_width = 0.35
        index = range(1, 13)
        bar1 = ax.bar(index, income_data, bar_width, label='Income')
        bar2 = ax.bar(index, expenses_data, bar_width, label='Expenses', bottom=income_data)

        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.set_title('Monthly Income and Expenses')
        ax.set_xticks(index)
        ax.set_xticklabels(months)
        ax.legend()

        plt.show()

    def start(self):
        self.content_frame()
        self.income_widgets()
        self.expenses_widgets()
        self.goals_widgets()
        # Add a button to plot the chart
        plot_button = Button(self.mainframe, text="Plot Chart", command=self.plot_chart)
        plot_button.grid(column=0, row=3, columnspan=3, sticky=W+E)

        self.window.mainloop()



def main():
    money_management = MoneyManagement()
    goals = Goals()
    gui = GUI_management(money_management, goals)
    gui.content_frame()
    gui.income_widgets()
    gui.expenses_widgets()
    gui.goals_widgets()
    gui.start()
    return 0

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
