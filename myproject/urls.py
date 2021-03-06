"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from manager import UserManager
from manager import PreferenceManager
from manager import VisitManager



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/users/$', UserManager.userRequest),  
    url(r'^api/users/(?P<user_id>\d*)/$', UserManager.userRequest),
    url(r'^api/users/(?P<user_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/$', UserManager.userRequest),
    url(r'^api/preferences/(?P<user_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/$', PreferenceManager.preferenceRequest  ),
    url(r'^api/preferences/(?P<user_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/lucky/$', PreferenceManager.randomPreference  ),
    url(r'^api/preferences/$', PreferenceManager.preferenceRequest ),
    url(r'^api/visit/$', VisitManager.visitRequest ),
    url(r'^api/visit/(?P<user_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/(?P<place_id>[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\\|,.<>\/?]*)/$', VisitManager.visitable ),
    url(r'^api/visit/favorite$', VisitManager.createFavorite ),
    url(r'^api/visit/(?P<user_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/favorite$', VisitManager.getFavorites ),
]
