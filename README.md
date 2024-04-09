# INST326-Financial-Manager
## This file provides functionality for:
- **Expense and income tracking**: Users can record, categorize, and view their expenses and incomes
- **Financial goals setting**: Users can set and track progress towards financial goals
- **Reports**: The program will generate text-based reports summarizing financial activity and goal progress
- **Data Visualization**: Charts(Bar/Line/Pie) to easily represent income and expense classes, track progress towards saving goals, or offer a quick look at how income is allocated across  different expense categories

## Currently In Progress:
- [ ] UI Implementation(Buttons, input boxes)
- [ ] Text Based reporting
- [ ] Data Visualization 

## Classes contained in this file
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
            <li> <code class="language-python">change_income(self, value: str) -> None</code></li>
            <li> <code class="language-python">adjust_expenses(self, value: str) -> None</code></li>
            <li> <code class="language-python">get_monthly_expenses(self, value: str) -> None</code></li>
            <li> <code class="language-python">get_monthly_income(self) -> float</code></li>
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
            <li> <code class="language-python">_get_month_num(self, month_name: str) -> int</code></li>
            <li> <code class="language-python">update_monthly_goal(self, goal: str, type: str, month: str = None) -> None</code></li>
            <li> <code class="language-python">get_monthly_goal(self, type: str) -> float</code></li>
            <li> <code class="language-python">update_yearly_income_goal(self, goal: str) -> None</code></li>
            <li> <code class="language-python">get_yearly_income_goal(self) -> float</code></li>
            <li> <code class="language-python">get_monthly_expense_goal(self) -> float</code></li>
            <li> <code class="language-python">update_yearly_expense_goal(self, goal: str) -> None</code></li>
            <li> <code class="language-python">get_yearly_expense_goal(self) -> float</code></li>
        </ol>
    </p>
</details>

<details>
    <summary>Gui Management</summary>
    <p>
        <b>Gui_management():</b> This class acts as a container for GUI related functions through tkinter. It will define a content frame and in time different tabs to access the project deliverables(data visualization, switching between income and expense, setting goals, etc). Upon initialization, it will define a window and a title for tkinter to operate on, along with initializing a Goals() and MoneyManagement() instance. Currently a WIP.
		<br>
        <b>Functions:</b>
        <ol type="1">
            <li> <code class="language-python">__init__(self)</code></li>
            <li> <code class="language-python">content_frame(self) -> None</code></li>
            <li> <code class="language-python">plugin_creation(self) -> None</code></li>
            <li> <code class="language-python">update_income(self, income_value) -> None</code></li>
            <li> <code class="language-python">start(self) -> None</code></li>
        </ol>
    </p>
</details>



## Sources/Documentation:
- [FreeCodeCamp datetime module](https://www.freecodecamp.org/news/python-get-current-time/#:~:text=How%20to%20Get%20the%20Current%20Time%20with%20the%20Time%20Module,the%20current%20date%20and%20time)
- [Programiz time module](https://www.programiz.com/python-programming/time)
- [Tkinter Documentation](https://tkdocs.com/index.html)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Private Methods in Python](https://www.geeksforgeeks.org/private-methods-in-python/)



## Notes for changes:
- Populate expenses and income dictionary with a default 0 to remove need for an exception class
- Assuming input will be handled in tkinter as a string but will research taking in respective values as they should be inputted, auto parse into floats for needed functions to avoid doing it in each function
- May separate classes into standalone files for readability
- Separate Readme class documentation for readability
- Fix the update_yearly_income_goal to match monthly by using an additional type specifier

