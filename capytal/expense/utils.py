"""
Utility functions related to the Expense model
"""


def balance_share(expense, recipient, nb_recipients):
    """Return the expense share of the recipient given the number of
    recipients concerned by it.

    If the recipient is the owner of the expense, the result will be positive,
    else, it will be negative.

    """
    share = expense.amount / nb_recipients
    if recipient == expense.owner:
        return share
    return -share