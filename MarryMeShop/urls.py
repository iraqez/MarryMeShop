from django.conf.urls import patterns, include, url
import catalog

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('marryshop.views',
                       # Examples:
                       # url(r'^$', 'MarryMeShop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
               #        url(r'^$', 'home', dict(template_name == 'index.html'), 'home'),
                       url(r'^$', 'home', dict(template_name = 'index.html'), 'home'),

                       url(r'^catalog/', include('catalog.urls', namespace="catalog")),

                       url(r'^admin/', include(admin.site.urls)),
                       )
