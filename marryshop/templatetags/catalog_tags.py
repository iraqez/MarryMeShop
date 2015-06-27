from django import template
from catalog.models import Category

register = template.Library()


@register.inclusion_tag("menu_sel.html")
def menu():
    subm = []
    menu_cat = Category.MENU
    for i in Category.objects.filter(first_menu=menu_cat[0][0]):
        subm.append(i)



    return {
        "menu_cat": menu_cat,
        "subm": subm,
    }


def submenu(menu_name):
    sub = Category.objects.filter(first_menu=menu_name)
    return {
        "sub": sub,
    }