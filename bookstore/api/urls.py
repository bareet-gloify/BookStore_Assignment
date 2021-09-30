# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # path("", views.apiOverview, name="apiOverview"),
    path("get-books/", views.getBooks, name="get-books"),
    path("get-book/<int:pk>", views.getBook, name="get-book"),
    path("add-book", views.addBook, name="add-book"),
    path("update-book/<int:pk>", views.updateBook, name="update-book"),
    path("delete-book/<int:pk>", views.deleteBook, name="delete-book")

]
