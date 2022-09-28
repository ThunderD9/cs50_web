from venv import create
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("categories", views.categories, name="categories"),
    path("listing/<int:id>", views.listing, name = "listing"),
    path("remove_watch/<int:id>", views.remove_watch, name="remove_watch"),
    path("add_watch/<int:id>", views.add_watch, name="add_watch"),
    path("watchlist", views.watchlist, name = "watchlist"),
    path("add_comment/<int:id>", views.add_comment, name = "add_comment"),
    path("add_bid/<int:id>", views.add_bid, name = "add_bid"),
    path("close_auction/<int:id>", views.close_auction, name = "close_auction")
]
