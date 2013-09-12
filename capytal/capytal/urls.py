from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capytal.views.home', name='home'),
    # url(r'^capytal/', include('capytal.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'capytal.views.homepage', name='homepage'),
    url(r'^expense/', include('expense.urls')),
    url(r'^roommate/', include('roommate.urls')),
)
