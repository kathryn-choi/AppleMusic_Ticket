from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listener_page, name='listener_page'),
]
