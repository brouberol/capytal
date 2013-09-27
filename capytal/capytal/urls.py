from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import expense_summary

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'capytal.views.home', name='home'),
    # url(r'^capytal/', include('capytal.foo.urls')),

    url(r'^admin/doc/', include(
        'django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'capytal.views.homepage', name='homepage'),
    url(r'^login/', 'capytal.views.user_login', name='user_login'),
    url(r'^logout/', 'capytal.views.user_logout',
        name='user_logout'),
    url(r'^expense/', include('expense.urls')),
    url(r'^roommate/', include('roommate.urls')),
    url(r'^(?P<cat_slug>[\w-]+)',
        expense_summary, name="roommate_expenses_by_category")
)
