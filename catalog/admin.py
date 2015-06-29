from django.contrib import admin
from catalog.models import Category, Product
from gallery.admin import ItemAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('first_menu', 'name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(ItemAdmin):
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)