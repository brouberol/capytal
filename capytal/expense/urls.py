"""
URLConfig of the expense app
"""

from django.conf.urls import patterns, url

from .views import ExpenseListView
from .views import ExpenseCreateView
from .views import ExpenseUpdateView
from .views import ExpenseDetailView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)$', ExpenseDetailView.as_view(), name="expense-display"),
    url(r'^$', ExpenseListView.as_view(), name="expense-list"),
    url(r'^new$', ExpenseCreateView.as_view(), name="expense-create"),
    url(r'^(?P<pk>\d+)/update$', ExpenseUpdateView.as_view(), name="expense-update"),
)
