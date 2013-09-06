from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'amount', 'date')
    list_filter = ('owner', 'date')
    search_fields = ('name',)

admin.site.register(Expense, ExpenseAdmin)
