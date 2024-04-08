# INST326-Financial-Manager
## This file provides functionality for:
- **Expense and income tracking**: Users can record, categorize, and view their expenses and incomes
- **Financial goals setting**: Users can set and track progress towards financial goals
- **Reports**: The program will generate text-based reports summarizing financial activity and goal progress
- **Data Visualization**: Charts(Bar/Line/Pie) to easily represent income and expense classes, track progress towards saving goals, or offer a quick look at how income is allocated across  different expense categories

## Currently In Progress:
1. UI Implementation(Buttons, input boxes)
2. Text Based reporting
3. Data Visualization 

<details>
		<summary>Classes contained in this file</summary>
<p><b>>MoneyManagement():</b> Class to manage income and expenses. Upon initilization, the class creates a dictionary to store income and expenses. It operates on a key:value pair of month[numeric]:value, i.e 
```python
self.income = {4:1000} 
```
	<b>Functions:</b>
	<ol type="1">
	<li> <code class="language-python">__init__(self)</code></li>
	<li> <code class="language-python">change_income(self, value: str) -> None<code></li>
	<li> <code class="language-python">adjust_expenses(self, value: str) -> None</code></li>
	<li> <code class="language-python">get_monthly_expenses(self, value: str) -> None</code></li>
	<li> <code class="language-python">get_monthly_income(self) -> float</code></li>
	<li> <code class="language-python">get_yearly_income(self) -> float</code></li>
	<li> <code class="language-python">get_yearly_expenses(self) -> float</code></li></p>

**Goals():** This class manages financial goals. Upon initilization, the class creates two dictionaries, one to handle goals for reducing your monthly expenses, and another to handle your monthly income goal. It also creates two floats to handle yearly income and expense goals, operating on the same month:value grouping
		**Functions:**
		1. `__init__(self)`
		2. `_get_month_num(self, month_name: str) -> int`[^1]
		3. `update_monthly_goal(self, goal: str, type: str, month: str = None) -> None`
		4. `get_monthly_goal(self, type: str) -> float`
		5. `update_yearly_income_goal(self, goal: str) -> None`
		6. `get_yearly_income_goal(self) -> float`
		7. `get_monthly_expense_goal(self) -> float
		8. `update_yearly_expense_goal(self, goal: str) -> None`
		9. `get_yearly_expense_goal(self) -> float`

**Gui_management():** This class acts as a container for GUI related functions through tkinter[^2]. It will define a content frame and in time different tabs to access the project deliverables(data visualization, switching between income and expense, setting goals, etc). Upon initilization it will define a window and a title for tkinter to operate on, along with initilizing a Goals() and MoneyManagement() instance. Currently a WIP.
	**Functions:**
	1. `__init__(self)`
	2. `content_frame(self) -> None`
	3. `plugin_creation(self) -> None`
	4. `update_income(self, income_value) -> None`
	5. `start(self) -> None`



## Sources/Documentation:
	* [FreeCodeCamp datetime module](https://www.freecodecamp.org/news/python-get-current-time/#:~:text=How%20to%20Get%20the%20Current%20Time%20with%20the%20Time%20Module,the%20current%20date%20and%20time)
	* [Programiz time module](https://www.programiz.com/python-programming/time)
	* [^2]:[Tkinter Documentation](https://tkdocs.com/index.html)
	* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
	* [^1]:[Private Methods in Python](https://www.geeksforgeeks.org/private-methods-in-python/)



## Notes for changes:
	* Populate expenses and income dictionary with a default 0 to remove need for an exception class
    * Assuming input will be handled in tkinter as a string but will research taking in respective values as they should be inputted, auto parse into floats for needed functions to avoid doing it in each function
	* May separate classes into standalone files for readability
	* Separate Readme class documentation for readability
	* Fix the update_yearly_income_goal to match monthly by using an additional type specifier

