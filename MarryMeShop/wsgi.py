"""
WSGI config for MarryMeShop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from django.conf import settings

#settings.configure()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MarryMeShop.settings")
application = get_wsgi_application()
