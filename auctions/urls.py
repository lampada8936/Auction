from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:auction>", views.auction_single, name="auction_single"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
