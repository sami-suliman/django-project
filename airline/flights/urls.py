from django.conf.urls import url

from . import views

urlpatterns = [
    url("<int:flight_id>/book", views.flight, name="book"),
    url("<int:flight_id>", views.flight, name="flight"),
    url("", views.index, name="index")
   # url(r'^myakun/$', 'portal.views.myakun', name='myakun'),
]