"""
WSGI config for MarryMeShop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MarryMeShop.settings")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('/var/www/django/MarryMeShop/MarryMeShop')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import django
django.setup()
