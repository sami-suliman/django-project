#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path("", views.index, name="index")
    url("", views.index, name="index"),
    url("world", views.world, name="world")
]