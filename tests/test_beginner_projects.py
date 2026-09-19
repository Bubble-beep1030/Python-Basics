import unittest

from projects.beginner.calculator.calculator import calculate
from projects.beginner.quiz.quiz import score_answers
from projects.beginner.file_organizer.file_organizer import group_by_extension


class TestBeginnerProjects(unittest.TestCase):
    def test_calculator_add(self):
        self.assertEqual(calculate('+', 2, 3), 5)

    def test_calculator_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate('/', 10, 0)

    def test_quiz_scoring(self):
        answers = {
            'Python uses indentation for code blocks': 'true',
            'List is immutable': 'false',
        }
        self.assertEqual(score_answers(answers), (2, 2))

    def test_file_organizer_groups(self):
        result = group_by_extension(['a.py', 'b.PY', 'README'])
        self.assertEqual(set(result.keys()), {'.py', '.no_ext'})


if __name__ == '__main__':
    unittest.main()
