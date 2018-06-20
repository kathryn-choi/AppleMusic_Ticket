from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.artist_list, name='artist_list'),
    url(r'^artist/(?P<pk>\d+)/$', views.artist_page, name='artist_page'),
]
