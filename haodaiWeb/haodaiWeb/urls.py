"""haodaiWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from web import views

# http://127.0.0.1:8000/detail/1023-20-24/
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^haodai/(?P<loc>.*)-(?P<money>\d+)-(?P<time>\d+)-(?P<page>\d+)/$', view=views.lists),
    url(r'^haodai/$', view=views.lists),
    url(r'^detail/(?P<id>\d+)-(?P<money>\d+)-(?P<time>\d+)/$',view=views.detail),

]
