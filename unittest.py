import unittest
from financial_management_tool import *

from datetime import datetime

class TestMoneyManagement(unittest.TestCase):
    """Test cases for the MoneyManagement class."""
    def setUp(self):
        """Create an instance of the MoneyManagement class before each test."""
        self.mm = MoneyManagement()


    def test_change_income(self, mock_datetime):
        """Test changing monthly income."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        self.mm.change_income('5000')
        self.assertEqual(self.mm.income[4], 5000.0)

    def test_adjust_expenses(self, mock_datetime):
        """Test adjusting monthly expenses."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        self.mm.adjust_expenses('3000')
        self.assertEqual(self.mm.expenses[4], 3000.0)

    def test_get_monthly_expenses_available(self, mock_datetime):
        """Test retrieving monthly expenses when available."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        self.mm.expenses[4] = 3000.0
        expenses = self.mm.get_monthly_expenses('3000')
        self.assertEqual(expenses, 3000.0)

    def test_get_monthly_expenses_unavailable(self, mock_datetime):
        """Test error when monthly expenses data is unavailable."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        with self.assertRaises(DataUnavailableError):
            self.mm.get_monthly_expenses('3000')


    def test_get_monthly_income_available(self, mock_datetime):
        """Test retrieving monthly income when available."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        self.mm.income[4] = 5000.0
        income = self.mm.get_monthly_income()
        self.assertEqual(income, 5000.0)


    def test_get_monthly_income_unavailable(self, mock_datetime):
        """Test error when monthly income data is unavailable."""
        mock_datetime.now.return_value = datetime(2024, 4, 1)
        with self.assertRaises(DataUnavailableError):
            self.mm.get_monthly_income()

    def test_get_yearly_income(self):
        """Test calculating total yearly income."""
        self.mm.income = {1: 1000.0, 2: 2000.0, 3: 3000.0}
        self.assertEqual(self.mm.get_yearly_income(), 6000.0)

    def test_get_yearly_expenses(self):
        """Test calculating total yearly expenses."""
        self.mm.expenses = {1: 500.0, 2: 1000.0, 3: 1500.0}
        self.assertEqual(self.mm.get_yearly_expenses(), 3000.0)

class TestGoals(unittest.TestCase):
    """Test cases for the Goals class."""

    def setUp(self):
        """Create an instance of the Goals class before each test."""
        self.goals = Goals()

    def test_update_and_get_monthly_goal(self):
        """Test updating and getting monthly income and expense goals."""
        self.goals.update_monthly_goal('4000', 'i')
        self.goals.update_monthly_goal('2000', 'e')
        self.assertEqual(self.goals.get_monthly_goal('i'), 4000.0)
        self.assertEqual(self.goals.get_monthly_goal('e'), 2000.0)

    def test_update_and_get_yearly_goals(self):
        """Test updating and getting yearly income and expense goals."""
        self.goals.update_yearly_income_goal('48000')
        self.goals.update_yearly_expense_goal('24000')
        self.assertEqual(self.goals.get_yearly_income_goal(), 48000.0)
        self.assertEqual(self.goals.get_yearly_expense_goal(), 24000.0)

    def test_invalid_month_name(self):
        """Test for handling invalid month names."""
        with self.assertRaises(DataUnavailableError):
            self.goals.update_monthly_goal('1000', 'i', 'NotAMonth')

class TestGuiManagement(unittest.TestCase):
    """Test cases for the GuiManagement class."""
    def setUp(self):
        """Create an instance of the Gui_management class before each test."""
        self.gui = GUI_management()

if __name__ == '__main__':
    unittest.main()
