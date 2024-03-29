
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.new_page, name="newpage"),
    path("randompage/", views.random_page, name = "randompage"),
    path("edit/", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit")
]
 