"""
Views of the roommate app
"""

from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.core.urlresolvers import reverse

from .models import Roommate
from .forms import UserCreateForm, UserUpdateForm


class RoommateDetailView(DetailView):
    model = Roommate


class RoommateListView(ListView):
    model = Roommate


class RoommateCreateView(CreateView):
    model = Roommate
    form_class = UserCreateForm

    def get_success_url(self):
        """Return the URL of the user account display"""
        r_id = Roommate.objects.get(user__id=self.object.id).id
        return reverse('roommate-display', kwargs={'pk': r_id})


class RoommateUpdateView(UpdateView):
    model = Roommate
    form_class = UserUpdateForm