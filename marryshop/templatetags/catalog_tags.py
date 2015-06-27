from django import template
from catalog.models import Category

register = template.Library()


@register.inclusion_tag("menu_sel.html")
def menu():
    menu_cat = Category.MENU
    # for i in Category.objects.filter(first_menu=menu_cat[0][0]):



    return {
        "menu_cat": menu_cat,
    }

# def menu():
#     menu_cat = Category.MENU
#     submenu1 = {}
#     for i in menu_cat:
#         submenu1[i[0]]=i[1]
#
#
#
#     return {
#         "menu_cat": submenu1,
#     }

def submenu(menu_name):
    sub = Category.objects.filter(first_menu=menu_name)
    return {
        "sub": sub,
    }