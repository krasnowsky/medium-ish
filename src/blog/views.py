from django.shortcuts import render

from .models import Article
# Create your views here.
def article_view(request):
    obj = Article.objects.get(id=1)
    '''context = {
        'title': obj.title,
        'content': obj.content,
        'author': obj.author,
        'date': obj.date,
    }'''
    context = {
        'obj': obj
    }
    return render(request, 'article.html', context)

'''def article_create_view(request):
    form = articleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = articleForm()

    context = {
        'form': form
    }

    return render(request, 'article_create.html', context)'''

def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html', {})

def tags_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Hello World</h1>')
    context = {
        'text': 'This is tag page',
        'number': 123,
        'list': [134, 212, 743, 43],
    }
    return render(request, 'tags.html', context)