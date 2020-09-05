from django.conf.urls import url
from . import views

app_name = "tasks"
urlpatterns = [
    url("add", views.add, name="add"),
    url("", views.index, name="index")
]