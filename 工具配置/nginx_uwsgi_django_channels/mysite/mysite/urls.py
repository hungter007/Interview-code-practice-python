# mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^AiGuess/', include('aiguess.urls')),
    url(r'^UserLogin/', include('userlogin.urls')),
    url(r'^admin/', admin.site.urls),
]