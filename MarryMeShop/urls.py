from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    'marryshop.views',
    # Examples:
    # url(r'^$', 'MarryMeShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^$', 'home', {
     #'template_name': 'index.html'}, 'home'),

     url(r'^admin/', include(admin.site.urls)),
     ]
