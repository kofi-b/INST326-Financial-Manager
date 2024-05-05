from tkinter import *
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 

import shelve

class DataUnavailableError(Exception):
    def __init__(self, message="Data is unavailable"):
        self.message = message
        super().__init__(self.message)

class DataPersistence:
    _filename = 'financial_management_data'

    def __init__(self):
        try:        
            with shelve.open(self._filename, 'c') as db:
                db.setdefault('data', {})
            print(f"File '{self._filename}' opened")
        except shelve.ShelfError as e:
            print(f"Error opening: {e}")
    
    def update_database(self, income=None, expenses=None, 
                        income_goal=None, expense_goal=None, 
                        yearly_income_goal=None, yearly_expense_goal=None) -> None:
        """
        Updates the shelve file with income, expense, and goal data.

        Args:
            income (float, optional): The user's monthly income.
            expenses (float, optional): The user's monthly expenses.
            income_goal (float, optional): The user's monthly income goal.
            expense_goal (float, optional): The user's monthly expense goal.
            yearly_income_goal (float, optional): The user's yearly income goal.
            yearly_expense_goal (float, optional): The user's yearly expense goal.
        """

        data = {}
        if income is not None:
            data['income'] = income
        if expenses is not None:
            data['expenses'] = expenses
        if income_goal is not None:
            data['income_goal'] = income_goal
        if expense_goal is not None:
            data['expense_goal'] = expense_goal
        if yearly_income_goal is not None:
            data['yearly_income_goal'] = yearly_income_goal
        if yearly_expense_goal is not None:
            data['yearly_expense_goal'] = yearly_expense_goal

        if data:
            try:
                with shelve.open(self._filename) as db:
                    db['data'] = data
                    print(f"Data updated")
            except shelve.ShelfError as e:
                print(f"Error updating data")

    def read_data(self):
        """
        Reads and returns the stored financial data from the shelve file.

        Returns:
            dict: A dictionary containing the stored financial data.
        """

        try:
            with shelve.open(self._filename) as db:
                data = db.get('data', {})
                return data
        except shelve.ShelfError as e:
            print(f"Error reading data: {e}")
            return {}



class MoneyManagement:
    """A class to manage income and expenses. Income and expenses work on a key:val pair of Month:value"""

    def __init__(self):
        self.income = {}
        self.expenses = {}

    def load_data(self, data: dict) -> None:
        income = data.get("income")
        for info in income.items():
            self.update_values(type="i", value=info[1], month=info[0])

        expenses = data.get("expenses")
        for info in expenses.items():
            self.update_values(type="e", value=info[1], month=info[0])

    def get_data(self):
        return self.income, self.expenses

    def update_values(self, type: str, value: float, month: str) -> None:
        if type == "i":
            self.income[month] = value
        else:
            self.expenses[month] = value

    def change_monthly_vals(self, value: str, type: str) -> None:
        """Change the monthly income/expenses for the current month.

        Args:
            value (str): The new income value.

        """
        if type == "i":
            income = float(value)
            currMonth = datetime.now().month
            self.income[currMonth] = income
        else:
            expenses = float(value)
            currMonth = datetime.now().month
            self.expenses[currMonth] = expenses

    def get_monthly_vals(self, value: str) -> None:
        """Get the monthly income/expenses for the current month.

        Returns:
            float: The monthly income.
            float: The monthly expenses.

        """
        if value == "e":
            curr_month = datetime.now().month

            return self.expenses[curr_month]
            
        else:
            curr_month = datetime.now().month
            
            return self.income[curr_month]
            
    
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

    def load_data(self, data) -> None:

        income = data.get("income_goal")
        for info in income.items():
            #print([info[0]])
            self.update_monthly_goal(goal=info[1], type="i", month=info[0])
        
        expense = data.get("expense_goal")
        for info in expense.items():
            self.update_monthly_goal(goal=info[1], type="e", month=info[0])

        #Get and set yearly data
        yearly_income = data.get("yearly_income_goal")
        yearly_expense = data.get("yearly_expense_goal")

        self.yearly_income_goal = yearly_income
        self.yearly_expense_goal = yearly_expense


        pass

    def get_data(self) -> None:
        return self.income_goal, self.expense_goal, self.yearly_income_goal, self.yearly_expense_goal
    

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
            month_num = month
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
            float: The monthly expense goal.

        """
        
        currMonth = datetime.now().month
        if type.lower() == "i":
            return self.income_goal[currMonth]
        else:
            return self.expense_goal[currMonth]
    
    def update_yearly_goal(self, goal: str, type: str) -> None:
        """Update the yearly income goal.

        Args:
            goal (str): The new yearly income goal.
            type (str): Specifies whether income[i] or expense[e]

        """
        if type.lower() == "i":
            self.yearly_income_goal = float(goal)
        else:
            self.yearly_expense_goal = float(goal)
    
    def get_yearly_goal(self, type: str) -> float:
        """Get the yearly income goal.

        Returns:
            float: The yearly income goal.

        """
        if type.lower() == "i":
            return self.yearly_income_goal
        else:
            return self.yearly_expense_goal
    




class GUI_management:
    def __init__(self, money_management, goals, persistence):
        self.window = Tk()
        self.window.title("Financial Management Tool")

        self.money_management = money_management
        self.goals = goals
        self.persistence = persistence



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
        self.money_management.change_monthly_vals(income_value, "i")

        #self.persistence.update_database(income=float(income_value))

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
        self.money_management.change_monthly_vals(expenses_value, "e")

        #self.persistence.update_database(expenses=float(expenses_value))

    def goals_widgets(self):
        goals_label = Label(self.mainframe, text="Goals:")
        goals_label.grid(column=0, row=2, sticky=W)

        self.goals_var = StringVar()
        goals_entry = ttk.Entry(self.mainframe, textvariable=self.goals_var)
        goals_entry.grid(column=1, row=2, sticky=(W,E))

        income_button = Button(self.mainframe, text="Income Goal", command=lambda: self.set_goal('i'))
        income_button.grid(column=2, row=2, sticky=W, padx=(2, 1))

        expense_button = Button(self.mainframe, text="Expense Goal", command=lambda: self.set_goal('e'))
        expense_button.grid(column=3, row=2, sticky=W, padx=(1, 4))


        
    def set_goal(self, type):
        goal_value = self.goals_var.get()
        if type.lower() == "i":
            self.goals.update_monthly_goal(goal_value, "i")
        else:
            self.goals.update_monthly_goal(goal_value, "e")


        #self.persistence.update_database(income_goal=float(goal_value))

    def on_closing(self):
        income, expenses = self.money_management.get_data()
        income_goal, expense_goal, yearly_income_goal, yearly_expense_goal = self.goals.get_data()

        self.persistence.update_database(income, expenses, income_goal, expense_goal,yearly_income_goal, yearly_expense_goal)
        self.window.destroy()




    def plot_chart(self):
        # Get monthly income and expenses data
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        income_data = [self.money_management.income.get(month, 0) for month in range(1, 13)]
        expenses_data = [self.money_management.expenses.get(month, 0) for month in range(1, 13)]
        income_goals = [self.goals.income_goal.get(month,0) for month in range(1, 13)]
        expense_goals = [self.goals.expense_goal.get(month,0) for month in range(1, 13)]   

        # Create a bar chart
        fig, ax = plt.subplots()
        bar_width = 0.35

        # Create a list of positions for expense bars with an offset that are side-by-side
        index = range(1, 13)
        bar1 = ax.bar(index, income_data, bar_width, label='Income')
        bar2 = ax.bar([i + bar_width for i in index], expenses_data, bar_width, label='Expenses')

        ax.scatter(index, income_goals, color='red', marker='*', label='Income Goal')
        ax.scatter([i + bar_width for i in index], expense_goals, color='red', marker='s', label='Expense Goal')


        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.set_title('Monthly Income and Expenses')
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(months)
        ax.legend()

        plt.show()

    def open_info_window(self):
        info_window = Toplevel(self.window)
        info_window.title("Monthly Report")

        curr_expenses = self.money_management.get_monthly_vals("e")
        curr_income = self.money_management.get_monthly_vals("i")

        yearly_income = self.money_management.get_yearly_income()
        yearly_expenses = self.money_management.get_yearly_expenses()

        income_goal = self.goals.get_monthly_goal("i")
        expense_goal = self.goals.get_monthly_goal("e")

        if curr_expenses > curr_income:
            percentage_text = f"Currently, your expenses are higher than your income by {curr_income/curr_expenses*100:.2f}%. "  
            income_goal_text = f"You set an income goal of ${income_goal:.2f}. "

            info_text = percentage_text + income_goal_text

            if income_goal > curr_income:
                info_text += "\n     * It looks like you might need to work a little harder to reach your income goal this month."
            else:
                info_text += "\n     * Keep up the good work! You surpassed your goal."
            
            info_text += f"\n\nYou set an expense goal of ${expense_goal:.2f}. Here's how it looks:"

            if expense_goal < curr_expenses:
                info_text += "\n    * It looks like you might need to adjust your spending habits to get lower your expenses and reach your goal. What innessential things can you cut out of your spending this month(i.e. Subscriptions, eating out, etc)."
            else:
                info_text += "\n    * Keep up the good work! You reduced your expenses below the goal"
        else:
            #This text occurs when their income > than monthly expenses
            percentage_text = f"Currently, your income is higher than your expenses by {curr_expenses/curr_income*100:.2f}%. "  
            income_goal_text = f"You set an income goal of ${income_goal:.2f}. "

            info_text = percentage_text + income_goal_text + "You're doing great so far by surpassing your current expenses, but lets check how far you are on achieving your goals:"

            if income_goal > curr_income:
                info_text += "\n    * It looks like you might need to work a little harder to reach your income goal this month."
            else:
                info_text += "\n    * Keep up the good work! You surpassed your goal."

            info_text += f"\n\nYou set an expense goal of ${expense_goal:.2f}. Here's how it looks:"

            if expense_goal < curr_expenses:
                info_text += "\n    * It looks like you might need to adjust your spending habits to get lower your expenses and reach your goal. What innessential things can you cut out of your spending this month(i.e. Subscriptions, eating out, etc). Although you are making more than you are losing, it never hurts to have more money"
            else:
                info_text += "\n    * Keep up the good work! You reduced your expenses below the goal"


        info_label = Label(info_window, text=info_text, justify=LEFT, wraplength=300)
        info_label.pack(padx=10, pady=10)


    def start(self):
        self.content_frame()
        self.income_widgets()
        self.expenses_widgets()
        self.goals_widgets()
        # Add a button to plot the chart
        plot_button = Button(self.mainframe, text="Plot Chart", command=self.plot_chart)
        plot_button.grid(column=0, row=3, columnspan=3, sticky=W+E)

        info_button = Button(self.mainframe, text="Monthly Report", command=self.open_info_window)
        info_button.grid(column=3, row=3, sticky=E)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()



def main():
    money_management = MoneyManagement()
    goals = Goals()
    persistence = DataPersistence()
    data = persistence.read_data()
    if data:
        money_management.load_data(data)
        goals.load_data(data)

    gui = GUI_management(money_management, goals, persistence)
    gui.content_frame()
    gui.income_widgets()
    gui.expenses_widgets()
    gui.goals_widgets()
    gui.start()
    #gui.protocol("WM_DELETE_WINDOW", gui.on_closing())
    return 0

if __name__ == "__main__":
    main()


