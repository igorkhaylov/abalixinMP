from django.urls import path
from main import views


urlpatterns = [
    path("", views.index, name="main"),
    path("article/<slug:slug>/", views.article_detail, name="article_detail"),
]
