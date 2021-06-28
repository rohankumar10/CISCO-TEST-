from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

