# -*- coding: utf-8 -*-

"""
Models related to expense categories.
"""

from django.db import models


class Category(models.Model):
    """A Category caracterizes the type of expense"""

    name = models.CharField(max_length=50, unique=True, verbose_name='nom')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = u"Catégorie"
        verbose_name_plural = u"Catégories"

    def __unicode__(self):
        return self.name
