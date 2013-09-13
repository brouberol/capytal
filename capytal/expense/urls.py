"""
URLConfig of the expense app
"""

from django.conf.urls import patterns, url

from .views import ExpenseListView
from .views import ExpenseCreateView
from .views import ExpenseUpdateView
from .views import ExpenseDetailView
from .views import ExpenseDeleteView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', ExpenseDetailView.as_view(), name="expense_display"),
    url(r'^$', ExpenseListView.as_view(), name="expense_list"),
    url(r'^new$', ExpenseCreateView.as_view(), name="expense_create"),
    url(r'^(?P<pk>\d+)/update$', ExpenseUpdateView.as_view(), name="expense_update"),
    url(r'^(?P<pk>\d+)/delete$', ExpenseDeleteView.as_view(), name="expense_delete"),
)
