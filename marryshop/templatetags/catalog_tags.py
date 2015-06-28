from django import template
from catalog.models import Category

register = template.Library()


@register.inclusion_tag("menu_sel.html")
def menu():
    subm = []
    menu_cat = Category.MENU
    for i in Category.objects.all():
        subm.append(i)

    return {
        "menu_cat": menu_cat,
        "subm": subm,
    }
