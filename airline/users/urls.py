from django.conf.urls import url

from . import views

urlpatterns = [
    url('logout', views.logout_view, name="logout"),
    url('login', views.login_view, name="login"),
    url("", views.index, name="index")
]