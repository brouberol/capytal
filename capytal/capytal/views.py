"""
General application wide views.
"""

from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from category.models import Category
from roommate.models import Roommate
from expense.models import Expense


def homepage(request, *args, **kwargs):
    """Display the website homepage"""
    return render_to_response('base.html', RequestContext(request))


def user_login(request, *args, **kwargs):
    """Log the user in"""
    return login(request, template_name='login.html', *args, **kwargs)


def user_logout(request, *args, **kwargs):
    """Log the user out and redirect him/her to the homepage"""
    logout(request, *args, **kwargs)
    return redirect('capytal.views.homepage')


def expense_summary(request, cat_slug):
    """Display the summary of the request roommate expenses for the given category"""
    roommate = get_object_or_404(Roommate, user=request.user)
    category = get_object_or_404(Category, slug=cat_slug)
    expense_list = Expense.objects.filter(category=category).order_by('-date')
    return render_to_response(
        'roommate/roommate_expense_category.html',
        {
            'roommate': roommate,
            'category': category,
            'expense_list': expense_list,
        },
        RequestContext(request))
