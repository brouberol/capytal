"""
Views of the expense app
"""

from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Expense


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseListView(ListView):
    model = Expense


class ExpenseCreateView(CreateView):
    model = Expense


class ExpenseUpdateView(UpdateView):
    model = Expense