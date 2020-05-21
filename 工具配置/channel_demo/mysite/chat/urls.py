# chat/urls.py
from django.conf.urls import url

from . import views
from .views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
