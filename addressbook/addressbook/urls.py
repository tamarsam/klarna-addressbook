
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^search/', include('search.urls')),
    url(r'^admin/', admin.site.urls),
]
