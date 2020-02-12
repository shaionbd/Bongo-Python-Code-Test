import unittest
from .distribute_expense import Expense


class TestExpensesMethod(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def _get_test_data(self):
        return [
            (
                [
                    {'user': 'user_1', 'amount': 60, 'shared_by': ['user_1', 'user_2', 'user_3']},
                    {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_3']}
                ],
                [
                    {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_1'},
                    {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_2'},
                ]
            ),
            (
                [
                    {'user': 'user_1', 'amount': 60, 'shared_by': ['user_1', 'user_2', 'user_3']},
                    {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_3']},
                    {'user': 'user_3', 'amount': 120, 'shared_by': ['user_1', 'user_2', 'user_3']},
                    {'user': 'user_1', 'amount': 90, 'shared_by': ['user_1', 'user_2']},
                ],
                [
                    {'payment_user': 'user_2', 'amount': 45.0, 'owe_to': 'user_1'},
                    {'payment_user': 'user_1', 'amount': 20.0, 'owe_to': 'user_3'},
                    {'payment_user': 'user_2', 'amount': 20.0, 'owe_to': 'user_3'}
                ]
            ),
            (
                [
                    {'user': 'user_1', 'amount': 90, 'shared_by': ['user_1', 'user_2', 'user_3']},
                    {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_3']},
                    {'user': 'user_3', 'amount': 230, 'shared_by': ['user_1', 'user_2', 'user_3']},
                    {'user': 'user_1', 'amount': 90, 'shared_by': ['user_1', 'user_2']},
                    {'user': 'user_2', 'amount': 220, 'shared_by': ['user_1', 'user_2', 'user_3']},
                ],
                [
                    {'payment_user': 'user_1', 'amount': 18.33, 'owe_to': 'user_2'},
                    {'payment_user': 'user_1', 'amount': 46.67, 'owe_to': 'user_3'},
                    {'payment_user': 'user_3', 'amount': 16.67, 'owe_to': 'user_2'}
                ]
            ),
            (
                [
                    {'user': 'user_1', 'amount': 60, 'shared_by': []},
                    {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_2']}
                ],
                [
                    {'payment_user': 'user_1', 'amount': 20.0, 'owe_to': 'user_2'}
                ]
            )
        ]

    def test_success_maze(self):
        expenses_list = self._get_test_data()

        for expense_info in expenses_list:
            expense_data, expected_output = expense_info
            expense = Expense(expense_data)
            self.assertEqual(expected_output, expense.find_distributed_expense())


if __name__ == '__main__':
    unittest.main()