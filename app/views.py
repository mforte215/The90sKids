from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Article


class IndexView(View):

    def get(self, request):
        articles = Article.objects.all().order_by("-date")
        context = {
            "articles": articles,
        }

        return render(request, "app/index.html", context)


class ArticleDetailView(View):

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        context = {
            "article": article,
        }

        return render(request, "app/article-detail.html", context)
