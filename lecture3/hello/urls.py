# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path("", views.index, name="index")
    # path("world", views.world, name="world")
    url("world", views.world, name="world"),
    url("<str:name>", views.greet, name="greet"),
    url("", views.index, name="index")
]