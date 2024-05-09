# INST326-Financial-Manager
## Description 
This is a financial management tool implemented in Python using the Tkinter library for the GUI and matplotlib for data visualization. It allows users to update their income and expenses, set monthly income goals, and view monthly financial data in a graphical format.

## Usage
Ensure Python and required packages (matplotlib) are installed on your system. To open the GUI, you can run the program by executing the main() function from the command line:
```sh
python financial_management_tool.py
```

## `finacial_management_tool` Functionality:
- **Expense and income tracking**: Users can record, categorize, and view their expenses and incomes
- **Financial goals setting**: Users can set and track progress towards financial goals
- **Reports**: The program will generate text-based reports summarizing financial activity and goal progress
- **Data Visualization**: The GUI includes a button to plot a bar chart showing monthly income and expenses.

## `tool_test` Functionality:
- **Creating instances of the three classes before each method: Ensures that each test method operates on a clean instance of the classes, preventing interference between tests.**
- **Testing the MoneyManagement class: Includes tests for initializing income and expenses, updating income and expenses for specific months, changing monthly income and expense values, and calculating total yearly income and expenses.**
- **Testing the Goals class:  Includes tests for initializing income and expense goals, updating monthly income and expense goals, updating yearly income and expense goals, and getting yearly income and expense goals.**
- **Includes tests for creating the main content frame of the GUI, including the layout and widgets for managing income, expenses, and goals.**


## Currently In Progress:
- [x] UI Implementation(Buttons, input boxes)
- [x] Text Based reporting
- [x] Data Visualization
- [x] Data Persistence 

## Classes contained in this file
<details>
    <summary>Data Persistence</summary>
    <p>
        <b>DataPersistence():</b> This class manages storage of all the financial values being operated upon in the program. Upon initialization, the class creates a database file called 'financial_management_data' or alternatively opens it if it exists. It provides functionality for updating values as they are entered and retriving in the form of a dictionary.
		<br>
        <b>Functions:</b>
        <ol type="1">
            <li> <code class="language-python">__init__(self)</code></li>
            <li> <code class="language-python">update_database(self, income=None, expenses=None, income_goal=None, expense_goal=None, yearly_income_goal=None, yearly_expense_goal=None) -> None</code></li>
            <li> <code class="language-python">read_data(self) -> None</code></li>
        </ol>
    </p>
</details>

<details>
    <summary>Money Management</summary>
    <p>
        <b>MoneyManagement():</b> Class to manage income and expenses. Upon initialization, the class creates a dictionary to store income and expenses. It operates on a key:value pair of month[numeric]:value, i.e:
		<br>
		<code class="language-python">self.income = {4:1000}</code>
	<br>
    <b>Functions:</b>
        <ol type="1">
            <li> <code class="language-python">__init__(self)</code></li>
            <li> <code class="language-python">load_data(self, data:dict) -> None</code></li>
            <li> <code class="language-python">get_data(self) -> None</code></li>
            <li> <code class="language-python">update_values(self, type: str, value: float, month: str) -> None</code></li>
            <li> <code class="language-python">change_monthly_vals(self, value: str, type:str) -> None</code></li>
            <li> <code class="language-python">get_monthly_vals(self, value: str) -> None</code></li>
            <li> <code class="language-python">get_yearly_income(self) -> float</code></li>
            <li> <code class="language-python">get_yearly_expenses(self) -> float</code></li>
        </ol>
    </p>
</details>

<details>
    <summary>Goals</summary>
    <p>
        <b>Goals():</b> This class manages financial goals. Upon initialization, the class creates two dictionaries, one to handle goals for reducing your monthly expenses, and another to handle your monthly income goal. It also creates two floats to handle yearly income and expense goals, operating on the same month:value grouping.
		<br>
        <b>Functions:</b>
        <ol type="1">
            <li> <code class="language-python">__init__(self)</code></li>
            <li> <code class="language-python">load_data(self, data:dict) -> None</code></li>
            <li> <code class="language-python">get_data(self) -> None</code></li>
            <li> <code class="language-python">update_monthly_goal(self, goal: str, type: str, month: str = None) -> None</code></li>
            <li> <code class="language-python">get_monthly_goal(self, type: str) -> float</code></li>
            <li> <code class="language-python">update_yearly_goal(self, goal: str, type: str) -> None</code></li>
            <li> <code class="language-python">get_yearly_goal(self, type: str) -> float</code></li>
        </ol>
    </p>
</details>

<details>
    <summary>GUI Management</summary>
    <p>
        <b>GUI_management():</b> This class acts as a container for GUI related functions through tkinter. It will define a content frame and in time different tabs to access the project deliverables(data visualization, switching between income and expense, setting goals, etc). Upon initialization, it will define a window and a title for tkinter to operate on, along with initializing a Goals() and MoneyManagement() instance. All methods have no return value.
		<br>
        <b>Functions:</b>
        <ol type="1">
            <li> <code class="language-python">__init__(self)</code></li>
            <li> <code class="language-python">content_frame(self)</code></li>
            <li> <code class="language-python">income_widgets(self)</code></li>
            <li> <code class="language-python">update_income(self)</code></li>
            <li> <code class="language-python">expenses_widgets(self)</code></li>
            <li> <code class="language-python">update_expenses(self)</code></li>
            <li> <code class="language-python">goals_widgets(self)</code></li>
            <li> <code class="language-python">set_goal(self, type)</code></li>
            <li> <code class="language-python">on_closing(self)</code></li>
            <li> <code class="language-python">plot_chart(self)</code></li>
            <li> <code class="language-python">open_info_window(self)</code></li>
            <li> <code class="language-python">start(self)</code></li>
        </ol>
    </p>
</details>



## Sources/Documentation:
- [FreeCodeCamp datetime module](https://www.freecodecamp.org/news/python-get-current-time/#:~:text=How%20to%20Get%20the%20Current%20Time%20with%20the%20Time%20Module,the%20current%20date%20and%20time)
- [Programiz time module](https://www.programiz.com/python-programming/time)
- [Tkinter Documentation](https://tkdocs.com/index.html)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [2nd Markdown Cheatsheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
- [Basic formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#links)
- [Private Methods in Python](https://www.geeksforgeeks.org/private-methods-in-python/)
- [Shelving in Python](https://docs.python.org/3/library/shelve.html)
- [Data Persistence in Python](https://www.tutorialspoint.com/python_data_persistence/python_data_persistence_quick_guide.htm)
- [matplotlib](https://matplotlib.org/stable/)
- [Tkinter protocols](https://web.archive.org/web/20201111215134/http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm#protocols)
- [Lambda Expressions](https://realpython.com/python-lambda/)




## Notes for changes:
- Populate expenses and income dictionary with a default 0 to remove need for an exception class
- May separate classes into standalone files for readability

