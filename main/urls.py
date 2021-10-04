from django.urls import path
from main import views


urlpatterns = [
    path("", views.index, name="main"),
    path("category/<slug:slug>/", views.category_view, name="category_view"),
    path("tests/", views.tests, name="tests"),
    path("podcasts/", views.podcasts, name="podcasts"),
    path("news/", views.news, name="news"),
    path("categories/", views.categories, name="categories"),
    path("article_detail/<slug:slug>/", views.article_detail, name="article_detail"),
    path("worldnews/<int:id>/", views.article_detail, name="world_news_detail"),
    path("uzbnews/<int:id>/", views.article_detail, name="uzb_news_detail"),
    path("see-more-categories/", views.DynamicArticles.as_view(), name="see-more-categories")
]
