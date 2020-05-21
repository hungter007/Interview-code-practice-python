from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'^myCreation', views.my_creation, name='myCreation'),
    url(r'^leaderBoard', views.leader_board, name='leaderBoard'),
]