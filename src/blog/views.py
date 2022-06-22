from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Article, Video, Tag

# Create your views here.
'''def article_view(request):
    obj1 = Article.objects.all()

    print(obj1[0].videos)

    context = {
        'obj': obj1,
    }
    return render(request, 'article.html', context)'''

def home_view(request, *args, **kwargs):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'home.html', context)

def tags_view(request, *args, **kwargs):
    tags = Tag.objects.all()

    tags_paginator = Paginator(tags, 5)

    page_num = request.GET.get('page')

    page = tags_paginator.get_page(page_num)

    context = {
        'page': page,
    }
    return render(request, 'tags.html', context)