from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    articles = Article.published.all()
    return render(request, "blog/all_articles.html", {"articles": articles})


def get_article(request, id, slug):
    # article = Article.objects.get(id=id, slug=slug)
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, "blog/article.html", {"article": article})
