from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    url(r'^view_router/(?P<id>[\w\.-]+)/', RouterDetail.as_view()),
    url(r'^get_router/(?P<router_id>[0-9]+)/', RouterData.as_view()),
    url(r'^add/', AddData.as_view()),
    url(r'^update/(?P<router_id>[0-9]+)/', RouterData.as_view()),
    url(r'^delete/(?P<router_id>[0-9]+)/', RouterDetail.as_view()),
    url(r'^add_many/', views.add_many),
    url(r'^login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
]
