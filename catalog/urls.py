from django.conf.urls import url, patterns
from catalog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
                       ]