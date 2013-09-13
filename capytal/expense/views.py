"""
Views of the expense app
"""

from django.views.generic import ListView, CreateView, UpdateView, DetailView, \
    DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin as _LoginRequiredMixin

from .models import Expense
from roommate.models import Roommate


class LoginRequiredMixin(_LoginRequiredMixin):
    login_url = reverse_lazy('user_login')
    redirect_field_name = 'next'


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense


class ExpenseListView(ListView):
    model = Expense

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        roommate = Roommate.objects.get(user=self.request.user)
        expenses = Expense.objects.filter(owner=roommate)
        context['balance'] = str(roommate.balance)
        context['expense_list'] = expenses
        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense

    def get_success_url(self):
        return reverse_lazy('expense_list')


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense

    def get_success_url(self):
        return reverse_lazy('expense_list')


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')