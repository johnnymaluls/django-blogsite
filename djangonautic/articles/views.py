
from django.shortcuts import render, redirect
from articles.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def articles_home(request):

    articles = Article.objects.all().order_by('date')
    # pass the articles variable into the articles_home.html to use it
    return render(request, 'articles/articles_home.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

# to require login


@login_required(login_url='/accounts/login')
def article_create(request):
    # to check for POST request
    if request.method == 'POST':
        # validates the data that we receive on the request object
        # request.FILES is needed when we include files
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to the database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')

    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
