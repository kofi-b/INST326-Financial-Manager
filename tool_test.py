import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from financial_management_tool import *
from unittest import mock


class TestMoneyManagement(unittest.TestCase):
    """Test cases for MoneyManagement class."""

    def setUp(self):
        self.money_management = MoneyManagement()

    def test_initialization(self):
        """Test initialization of MoneyManagement class."""
        self.assertEqual(self.money_management.income, {})
        self.assertEqual(self.money_management.expenses, {})

    def test_update_values_income(self):
        """Test updating income values."""
        self.money_management.update_values("i", 1000.0, "January")
        self.assertEqual(self.money_management.income["January"], 1000.0)

    def test_update_values_expenses(self):
        """Test updating expenses values."""
        self.money_management.update_values("e", 500.0, "February")
        self.assertEqual(self.money_management.expenses["February"], 500.0)

    def test_change_monthly_vals_income(self):
        """Test changing monthly income values."""
        self.money_management.change_monthly_vals("1500.0", "i")
        curr_month = datetime.now().month
        self.assertEqual(self.money_management.income[curr_month], 1500.0)

    def test_change_monthly_vals_expenses(self):
        """Test changing monthly expenses values."""
        self.money_management.change_monthly_vals("700.0", "e")
        curr_month = datetime.now().month
        self.assertEqual(self.money_management.expenses[curr_month], 700.0)

    def test_get_monthly_vals_income(self):
        """Test getting monthly income values."""
        self.money_management.change_monthly_vals("2000.0", "i")
        self.assertEqual(self.money_management.get_monthly_vals("i"), 2000.0)

    def test_get_monthly_vals_expenses(self):
        """Test getting monthly expenses values."""
        self.money_management.change_monthly_vals("1000.0", "e")
        self.assertEqual(self.money_management.get_monthly_vals("e"), 1000.0)

    def test_get_yearly_income(self):
        """Test calculating total yearly income."""
        money_management = MoneyManagement()
        money_management.income = {1: 1000.0, 2: 2000.0, 3: 3000.0}
        self.assertEqual(money_management.get_yearly_income(), 6000.0)

    def test_get_yearly_expenses(self):
        """Test calculating total yearly expenses."""
        money_management = MoneyManagement()
        money_management.expenses = {1: 500.0, 2: 1000.0, 3: 1500.0}
        self.assertEqual(money_management.get_yearly_expenses(), 3000.0)


class TestGoals(unittest.TestCase):
    """Test cases for Goals class."""

    def setUp(self):
        self.goals = Goals()

    def test_initialization(self):
        """Test initialization of Goals class."""
        self.assertEqual(self.goals.income_goal, {})
        self.assertEqual(self.goals.expense_goal, {})
        self.assertEqual(self.goals.yearly_income_goal, 0.0)
        self.assertEqual(self.goals.yearly_expense_goal, 0.0)

    def test_update_monthly_goal_income(self):
        """Test updating monthly income goal."""
        self.goals.update_monthly_goal("1500.0", "i", "January")
        self.assertEqual(self.goals.income_goal["January"], 1500.0)

    def test_update_monthly_goal_expense(self):
        """Test updating monthly expense goal."""
        self.goals.update_monthly_goal("700.0", "e", "February")
        self.assertEqual(self.goals.expense_goal["February"], 700.0)

    def test_update_yearly_goal_income(self):
        """Test updating yearly income goal."""
        self.goals.update_yearly_goal("25000.0", "i")
        self.assertEqual(self.goals.yearly_income_goal, 25000.0)

    def test_update_yearly_goal_expense(self):
        """Test updating yearly expense goal."""
        self.goals.update_yearly_goal("18000.0", "e")
        self.assertEqual(self.goals.yearly_expense_goal, 18000.0)

    def test_get_yearly_goal_income(self):
        """Test getting yearly income goal."""
        self.goals.update_yearly_goal("30000.0", "i")
        self.assertEqual(self.goals.get_yearly_goal("i"), 30000.0)

    def test_get_yearly_goal_expense(self):
        """Test getting yearly expense goal."""
        self.goals.update_yearly_goal("20000.0", "e")
        self.assertEqual(self.goals.get_yearly_goal("e"), 20000.0)



class TestGUIManagement(unittest.TestCase):
    """Test cases for GUI_management class."""

    def setUp(self):
        self.gui = GUI_management(MagicMock(), MagicMock(), MagicMock())

    @patch('financial_management_tool.tkinter.Tk.mainloop')
    @patch('financial_management_tool.tkinter.Tk.protocol')
    def test_start(self, mock_protocol, mock_mainloop):
        """Test starting GUI."""
        self.gui.start()
        self.gui.content_frame.assert_called_once()
        self.gui.income_widgets.assert_called_once()
        self.gui.expenses_widgets.assert_called_once()
        self.gui.goals_widgets.assert_called_once()
        mock_protocol.assert_called_once_with("WM_DELETE_WINDOW", self.gui.on_closing)
        mock_mainloop.assert_called_once()

    @patch('financial_management_tool.tkinter.ttk.Frame')
    @patch('financial_management_tool.tkinter.Tk')
    def test_content_frame(self, mock_Tk, mock_Frame):
        """Test creating content frame."""
        self.gui.content_frame()
        mock_Tk.assert_called_once()
        mock_Tk.return_value.title.assert_called_once_with("Financial Management Tool")
        mock_Frame.assert_called_once_with(self.gui.window, padding="3 3 12 12")
        self.gui.window.grid.assert_called_once_with(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
        self.gui.window.columnconfigure.assert_called_once_with(0, weight=1)
        self.gui.window.rowconfigure.assert_called_once_with(0, weight=1)

    @patch('financial_management_tool.Label')
    @patch('financial_management_tool.ttk.Entry')
    @patch('financial_management_tool.Button')
    def test_income_widgets(self, mock_Button, mock_Entry, mock_Label):
        """Test creating income widgets."""
        self.gui.mainframe = MagicMock()
        self.gui.income_widgets()
        mock_Label.assert_called_once_with(self.gui.mainframe, text="Income:")
        mock_Entry.assert_called_once_with(self.gui.mainframe, textvariable=self.gui.income_var)
        mock_Button.assert_called_once_with(self.gui.mainframe, text="Update Income", command=self.gui.update_income)

    @patch('financial_management_tool.Label')
    @patch('financial_management_tool.ttk.Entry')
    @patch('financial_management_tool.Button')
    def test_expenses_widgets(self, mock_Button, mock_Entry, mock_Label):
        """Test creating expenses widgets."""
        self.gui.mainframe = MagicMock()
        self.gui.expenses_widgets()
        mock_Label.assert_called_once_with(self.gui.mainframe, text="Expenses:")
        mock

if __name__ == "__main__":
    main()

