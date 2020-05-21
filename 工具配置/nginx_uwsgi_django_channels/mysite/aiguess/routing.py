# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^aiGuess/room/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^aiGuess/playing/(?P<room_name>[^/]+)/$', consumers.PlayingConsumer),
]