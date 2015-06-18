from django.contrib import admin
from catalog.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first_menu', 'name',)
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)
