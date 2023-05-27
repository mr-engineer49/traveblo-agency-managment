from django.contrib import admin
from .models import Action



# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    actions_lst = ['Category']
admin.site.register(Action, CategoryAdmin)
