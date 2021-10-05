# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("get-users/", views.UserAPIView.as_view()),
    path("post-user", views.UserAPIView.as_view()),
    path("update-user/<int:pk>", views.UserAPIView.as_view()),
    path("delete-user/<int:pk>", views.UserAPIView.as_view()),
    path("get-user/<int:pk>", views.UserDetailAPIView.as_view()),


    path("get-bookstores/", views.BookStoreAPIView.as_view()),
    path("post-bookstore", views.BookStoreAPIView.as_view()),
    path("update-bookstore/<int:pk>", views.BookStoreAPIView.as_view()),
    path("delete-bookstore/<int:pk>", views.BookStoreAPIView.as_view()),
    path("get-bookstore/<int:pk>", views.BookStoreDetailAPIView.as_view()),

    path("get-books/", views.BookAPIView.as_view()),
    path("post-book", views.BookAPIView.as_view()),
    path("update-book/<int:pk>", views.BookAPIView.as_view()),
    path("delete-book/<int:pk>", views.BookAPIView.as_view()),
    path("get-book/<int:pk>", views.BookDetailAPIView.as_view()),

]
