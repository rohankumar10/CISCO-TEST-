from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^view_router/', RouterDetail.as_view()),
    url(r'^get_router/(?P<router_id>[0-9]+)/', RouterData.as_view()),
    url(r'^add/', AddData.as_view()),
    url(r'^update/(?P<router_id>[0-9]+)/', RouterData.as_view()),
    url(r'^delete/(?P<router_id>[0-9]+)/', RouterDetail.as_view()),
    url(r'^add_many/', views.add_many),
]
