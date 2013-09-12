# -*- coding: utf-8 -*-

"""
Forms related to roommates
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm as auth_UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(auth_UserCreationForm):
    """
    User register form

    Technically, you can use this form to update an existing instance, but it
    is not recommanded since the username can be changed.

    Note that only the creation of an instance is garanteed.
    """
    first_name = forms.CharField(max_length=30, label=u"Prénom")
    last_name = forms.CharField(max_length=30, label=u"Nom")
    email = forms.EmailField(label=u"Adresse mail")

    def save(self, commit=True, *args, **kwargs):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(ModelForm):
    """
    User update form.

    This form is a classic model form, but you can't update the user name.

    Note that only update is garanteed to be working.

    """
    username = None

    def clean_email(self):
        if not self.cleaned_data.get('email'):
            raise forms.ValidationError(u'Le champ \'email\' est obligatoire.')
            return
        else:
            return self.cleaned_data['email']

    def clean_first_name(self):
        if not self.cleaned_data.get('first_name'):
            raise forms.ValidationError(u'Le champ \'prénom\' est obligatoire.')
            return
        else:
            return self.cleaned_data['first_name']

    def clean_last_name(self):
        if not self.cleaned_data.get('last_name'):
            raise forms.ValidationError(u'Le champ \'nom\' est obligatoire.')
            return
        else:
            return self.cleaned_data['last_name']

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
