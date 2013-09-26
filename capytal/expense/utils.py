"""
Utility functions related to the Expense model
"""

from __future__ import division


def balance_share(expense, recipient, nb_recipients):
    """Return the expense share of the recipient given the number of
    recipients it concerns.

    If the recipient is the owner of the expense, the result will be positive,
    else, it will be negative.

    """
    if recipient == expense.owner:
        return (nb_recipients - 1) * expense.amount / nb_recipients
    return -expense.amount / nb_recipients
