from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from catalog.models import Category


def menuSel():
    submenu = Category.objects.all()
    context = RequestContext(request, {'submenu': submenu})
    return HttpResponse(template.render(submenu))
