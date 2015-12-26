from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'',include('blog.urls')),  #per gli urls guardare http://tutorial.djangogirls.org/it/django_urls/index.html parte 13
]
