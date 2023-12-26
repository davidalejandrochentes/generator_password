from django.urls import path
from . import views

urlpatterns = [
    path('generator/', views.index, name="index"),
    path('', views.about, name="about"),
    path('password/', views.password, name="password")
]
