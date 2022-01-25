from django.urls import path
from Digikull_com import views
urlpatterns = [
    path('home', views.Home, name="home"),
    path('shorten', views.Shorten, name="shorten"),
    path("<str:pk>", views.Original, name="original")
]
