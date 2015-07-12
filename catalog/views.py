from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext, loader
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from catalog.models import Category, Product


def index(request):
    return render(request, 'catalog/templates/index.html')
    # template = loader.get_template('catalog/templates/index.html')
    # page_title = 'Marry-Me все для свадеб'
    # return render_to_response(template,)#, locals(), context_instance=RequestContext(request))

#
# def show_category(request, category_slug, template_name="catalog/index.html"):
#     p = get_object_or_404(Category, slug=category_slug)
