import unittest

from projects.intermediate.expense_tracker.expense_tracker import (
    Expense,
    add_expense,
    category_totals,
)
from projects.intermediate.contact_manager.contact_manager import add_contact, find_contact
from projects.intermediate.text_analyzer.text_analyzer import word_frequency
from projects.advanced.automation_workflow_capstone.stage_1.pipeline import normalize_tasks


class TestIntermediateProjects(unittest.TestCase):
    def test_expense_tracker_totals(self):
        data: list[Expense] = []
        add_expense(data, 'Food', 20)
        add_expense(data, 'food', 5)
        self.assertEqual(category_totals(data)['food'], 25)

    def test_expense_invalid_amount(self):
        data: list[Expense] = []
        with self.assertRaises(ValueError):
            add_expense(data, 'food', 0)

    def test_contact_manager(self):
        book = {}
        add_contact(book, 'Alice', '12345')
        self.assertEqual(find_contact(book, 'alice'), '12345')

    def test_text_analyzer(self):
        result = word_frequency('Hello, hello world!')
        self.assertEqual(result['hello'], 2)
        self.assertEqual(result['world'], 1)

    def test_capstone_stage1_normalize(self):
        tasks = normalize_tasks([{'name': '  task1 '}, {'name': ''}, {'done': True}])
        self.assertEqual(tasks, [{'name': 'task1', 'done': False}])


if __name__ == '__main__':
    unittest.main()
