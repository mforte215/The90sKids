from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>", views.ArticleDetailView.as_view(), name="article-detail")
]
