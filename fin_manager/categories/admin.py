from django.contrib import admin

from fin_manager.categories.models import Category, Entry

admin.site.register(Category)
admin.site.register(Entry)
