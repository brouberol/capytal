"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from expense.models import Expense
from category.models import Category
from roommate.models import Roommate



class ExpenseTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='test1')
        self.user2 = User.objects.create(username='test2')
        self.user3 = User.objects.create(username='test3')
        self.category = Category.objects.create(name='test_category')

    def test_add_expense_to_single_recipient(self):
        roommate = Roommate.objects.get(user=self.user1)
        expense = Expense.objects.create(owner=roommate, amount=10.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate)
        # reload roommate object
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)

    def test_add_expense_to_several_recipients(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2, roommate3)
        # reload roommate objects
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)

    def test_modify_expense_amount(self):
        roommate = Roommate.objects.get(user=self.user1)
        expense = Expense.objects.create(owner=roommate, amount=10.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate)
        # reload roommate object
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)
        # modify expense amount
        expense.amount = 20.0
        expense.save()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)

    def test_modify_expense_amount_with_several_recipients(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2, roommate3)
        # reload roommate object
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)
        # modfify expense amount
        expense.amount = 12.0
        expense.save()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 8.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -4.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -4.0)

    def test_add_recipients(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)
        expense.recipients.add(roommate2, roommate3)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)

    def test_remove_recipients(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 3.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -3.0)

        expense.recipients.remove(roommate2)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)


    def test_modify_expense_but_keep_amount(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2, roommate3)
        # reload roommate object
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)
        # modify expense amount
        expense.name = 'plop'
        expense.save()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)

    def test_delete_expense(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2, roommate3)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)
        expense.delete()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, 0.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, 0.0)

    def test_delete_expense_with_several_recipients(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense.recipients.add(roommate1, roommate2, roommate3)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)
        expense.delete()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, 0.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, 0.0)

    def test_add_multiple_expenses_with_several_recipients_then_delete_one(self):
        roommate1 = Roommate.objects.get(user=self.user1)
        roommate2 = Roommate.objects.get(user=self.user2)
        roommate3 = Roommate.objects.get(user=self.user3)
        expense1 = Expense.objects.create(owner=roommate1, amount=6.0,
                                         name='test_expense', category=self.category)
        expense2 = Expense.objects.create(owner=roommate2, amount=12.0,
                                         name='test_expense', category=self.category)
        expense1.recipients.add(roommate1, roommate2, roommate3)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, -2.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -2.0)

        expense2.recipients.add(roommate1, roommate2, roommate3)
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, 0.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, 6.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -6.0)

        expense1.delete()
        self.assertEqual(Roommate.objects.get(user=self.user1).balance, -4.0)
        self.assertEqual(Roommate.objects.get(user=self.user2).balance, 8.0)
        self.assertEqual(Roommate.objects.get(user=self.user3).balance, -4.0)
