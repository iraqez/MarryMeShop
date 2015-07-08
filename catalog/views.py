from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from catalog.models import Category, Product


def show_category(request, category_slug, template_name="catalog/index.html"):
    p = get_object_or_404(Category, slug=category_slug)
