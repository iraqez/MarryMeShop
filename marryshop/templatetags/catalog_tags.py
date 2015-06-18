from django import template
from catalog.models import Category

register = template.Library()


@register.inclusion_tag("menu_sel.html")
def menu():
    menu_cat = Category.MENU

    return {
        "menu_cat": menu_cat,
    }


def submenu(request, menu_name):
    sub = Category.objects.filter(first_menu=menu_name)
    return {
        "sub": sub,
    }
