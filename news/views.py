from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Count
from news.models import Category, News
from django.db.models import Count

# Create your views here.

menu = [
    {"title": "Home", "url":"home"},
    {"title": "About", "url":"about"},
    {"title": "Contact", "url":"contact"},
]


def index(request):

    context = {
        "title":"Home", 
        "menu": menu,
        "posts" : News.objects.all(),
        "categories": Category.objects.all(),
        "cat_selected": 0,
    }

    return render(request, "news/index.html", context)


def error(request):
    context = {
        "title":"Error"
    }
    return render(request, "news/error.html", context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Not Found")

def categories(request, cat_id):
    news = News.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()

    if len(news) == 0:
        raise Http404()
    
    context = {
        "news": news,
        "categories": cat,
        "cat_selected": cat_id,
        "title": "Categories",
    }
    # return HttpResponseNotFound(f"Category - {cat_id}")
    return render(request, "news/categories.html", context)

def categories_list(request):
    cat = Category.objects.all().annotate(news_count=Count('newss'))

    context = { 
        "categories": cat,
        "title": "Categories",
    }
    
    return render(request, "news/categories_list.html", context)



def news_detail(request, news_id):
    context = {
        "target_news": News.objects.get(id=news_id),
        "title": "Categories",
    }
    return render(request, "news/standard-formate.html", context)