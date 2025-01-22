from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_note', views.new_note, name="new_note"),
]
