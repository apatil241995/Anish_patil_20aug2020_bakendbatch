from django.urls import path
from Account import views
urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path("singup", views.singup, name="singup"),
    path("register", views.Register, name="register")
]