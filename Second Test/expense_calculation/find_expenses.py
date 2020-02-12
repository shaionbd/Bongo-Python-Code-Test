

class Expense:
    def __init__(self, expenses):
        self.expenses = expenses
        self.output = []

    def find_payer(self):
        find_user_expenses = []
        per_user_total_cost = {}
        for exp in self.expenses:
            exp_user, amount, exp_share_users = exp['user'], exp['amount'], exp['shared_by']
            if exp_share_users:
                shared_amount = float(amount / len(exp_share_users))
                for user in exp_share_users:
                    if user == exp_user:
                        pass
                    else:
                        find_user_expenses.append({"payment_user": user, "amount": shared_amount, "owe_to": exp_user})
            else:
                find_user_expenses.append({'payment_user': '', "own_cost": amount, "amount": 0, "owe_to": []})
        return find_user_expenses


if __name__ == '__main__':
    expense_input_1 = [
        {'user': 'user_1', 'amount': 60, 'shared_by': ['user_1', 'user_2', 'user_3']},
        {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_3']}
    ]
    expense_input_2 = [
        {'user': 'user_1', 'amount': 60, 'shared_by': ['user_1', 'user_2', 'user_3']},
        {'user': 'user_2', 'amount': 40, 'shared_by': ['user_1', 'user_3']},
        {'user': 'user_3', 'amount': 120, 'shared_by': ['user_1', 'user_2', 'user_3']},
        {'user': 'user_1', 'amount': 90, 'shared_by': ['user_1', 'user_2']},
    ]

    """
    # Output
    [
        {payment_user: 'user_3', 'amount': 20, owe_to: 'user_1'},
        {payment_user: 'user_3', 'amount': 20, owe_to: 'user_2'},
    ]
    # Test 1
        [
            {'payment_user': 'user_2', 'amount': 20.0, 'owe_to': 'user_1'}, 
            {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_1'}, 
            {'payment_user': 'user_1', 'amount': 20.0, 'owe_to': 'user_2'}, 
            {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_2'}
        ]
    # Test 2
        [
            {'payment_user': 'user_2', 'amount': 20.0, 'owe_to': 'user_1'}, 
            {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_1'}, 
            {'payment_user': 'user_1', 'amount': 20.0, 'owe_to': 'user_2'}, 
            {'payment_user': 'user_3', 'amount': 20.0, 'owe_to': 'user_2'}, 
            {'payment_user': 'user_1', 'amount': 40.0, 'owe_to': 'user_3'}, 
            {'payment_user': 'user_2', 'amount': 40.0, 'owe_to': 'user_3'}
        ]
    """
    expense = Expense(expense_input_2)
    print(expense.find_payer())
