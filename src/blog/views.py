from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Article, Tag, Author

# Create your views here.

def home_view(request, *args, **kwargs):
    articles = Article.objects.all()

    articles_paginator = Paginator(articles, 5)
    page_num = request.GET.get('page')
    page = articles_paginator.get_page(page_num)

    context = {
        'page': page,
    }
    return render(request, 'home.html', context)

def article_view(request, *args, **kwargs):
    slug = kwargs.get('slug')

    article = Article.objects.get(slug=slug)

    context = {
        'article': article,
    }

    return render(request, 'article_detail.html', context)

def author_view(request, *args, **kwargs):
    slug = kwargs.get('slug')

    author = Author.objects.get(slug=slug)

    context = {
        'author': author,
    }

    return render(request, 'author_detail.html', context)

def tags_view(request, *args, **kwargs):
    tags = Tag.objects.all()

    tags_paginator = Paginator(tags, 5)
    page_num = request.GET.get('page')
    page = tags_paginator.get_page(page_num)

    context = {
        'page': page,
    }
    return render(request, 'tags.html', context)