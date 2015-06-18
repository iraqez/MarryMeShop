# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect

from catalog.models import Category


def home(request, template_name="index.html"):
    page_title = "Свадебные аксесуары и все для свадьбы"

    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
