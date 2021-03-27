from django.urls import path
from .import views


app_name = 'articles'

urlpatterns = [

    path('', views.articles_home, name="list"),
    path('create/', views.article_create, name="create"),
    # where the first slug "<slug" is the type of the passed parameter which is a slug in our case,
    # and the second slug ":slug>" is the name of the parameter which could be any name; "abc", "the_slug", etc.
    path('<slug:slug>/', views.article_detail, name="detail"),
]
