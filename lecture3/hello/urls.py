# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path("", views.index, name="index")
    # path("world", views.world, name="world")
    url("", views.index, name="index"),
    url("<str:name>", views.greet, name="greet"),
    url("world", views.world, name="world")
]