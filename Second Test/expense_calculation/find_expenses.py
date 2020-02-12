"""
Time & Space Complexity:
Time Complexity: O(NxM) # N = Number of expenses; M = Number of Users
Space Complexity: O(NxM)
"""

class Expense:
    def __init__(self, expenses):
        self.expenses = expenses
        self.output = []
        self.expense_queue = []

    def __get_distribute_expenses(self):
        while self.expense_queue:
            # get user all info
            user_info = self.expense_queue.pop(0)
            # get payment user and owe to user from expense queue
            payment_user, amount, owe_to = user_info['payment_user'], user_info['amount'], user_info['owe_to']
            remain_amount = amount # first assume payee user has to give `remain_amount` of money to Owe user
            # new expense queue take all remain expenses from `expense_queue`
            # where `payment_user` and `owe_to` are not involed
            new_expense_queue = []
            for payment_index in range(len(self.expense_queue)):
                # get current index user
                cur_user_info = self.expense_queue[payment_index]
                cur_payment_user, cur_amount, cur_owe_to = cur_user_info['payment_user'], cur_user_info['amount'], cur_user_info['owe_to']
                # check whether current payment and owe user are involved to main user
                # if `True` then calculate remain mount
                # Otherwise insert to new queue
                if payment_user == cur_payment_user and owe_to == cur_owe_to:
                    remain_amount += float(cur_amount)
                elif payment_user == cur_owe_to and owe_to == cur_payment_user:
                    remain_amount -= float(cur_amount)
                else:
                    new_expense_queue.append(self.expense_queue[payment_index])
            # check who got the remain amount
            if int(remain_amount) != 0:
                if remain_amount < 0:
                    self.output.append({"payment_user": owe_to, "amount": round(abs(remain_amount), 2), "owe_to": payment_user})
                else:
                    self.output.append({"payment_user": payment_user, "amount": round(remain_amount, 2), "owe_to": owe_to})
            self.expense_queue = new_expense_queue
        return self.output

    def find_distributed_expense(self):
        for exp in self.expenses:
            # find expense sharer from current expense
            exp_user, amount, exp_share_users = exp['user'], exp['amount'], exp['shared_by']
            if exp_share_users:
                # Insert share amount to queue
                shared_amount = float(amount / len(exp_share_users))
                for user in exp_share_users:
                    if user != exp_user:
                        self.expense_queue.append({
                            "payment_user": user, "amount": shared_amount, "owe_to": exp_user
                        })
        return self.__get_distribute_expenses()


if __name__ == '__main__':
    expense_input = [
        {'user': 'user_1', 'amount': 60, 'shared_by': ['user_1', 'user_2', 'user_3']},
        {'user': 'user_2', 'amount': 40, 'shared_by': ['user_2', 'user_4']},
        {'user': 'user_3', 'amount': 120, 'shared_by': ['user_1', 'user_3', 'user_3']},
        {'user': 'user_1', 'amount': 90, 'shared_by': ['user_1', 'user_2']},
        {'user': 'user_3', 'amount': 45, 'shared_by': ['user_1', 'user_2','user_3','user_4']},
        {'user': 'user_4', 'amount': 90, 'shared_by': ['user_4', 'user_3']},
    ]
    expense = Expense(expense_input)
    distributed_exp = expense.find_distributed_sexpense()
    print(distributed_exp)
