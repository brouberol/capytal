"""
General application wide views.
"""

from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext


def homepage(request, *args, **kwargs):
    """Display the website homepage"""
    return render_to_response('base.html', RequestContext(request))


def user_login(request, *args, **kwargs):
    """Log the user in"""
    return login(request, template_name='login.html', *args, **kwargs)


def user_logout(request, *args, **kwargs):
    return logout(request, template_name='base.html', *args, **kwargs)