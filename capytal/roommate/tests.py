"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Roommate


class RoommateTest(TestCase):

    def test_generate_slug_at_save(self):
        """Checks that the Roommate slug is generated when saved."""
        user = User.objects.create(username='test1')
        user.save()
        roommate = Roommate.objects.get(user=user)
        self.assertEqual(roommate.slug, 'test1')

    def test_generate_slug_at_save_with_complicated_username(self):
        """Checks that the Roommate slug is generated when saved."""
        user = User.objects.create(username='stormagan the bold')
        user.save()
        roommate = Roommate.objects.get(user=user)
        self.assertEqual(roommate.slug, 'stormagan-the-bold')
