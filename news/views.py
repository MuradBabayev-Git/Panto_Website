from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
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


def news_detail(request, news_id):
    context = {
        "target_news": News.objects.get(id=news_id),
        "title": "Categories",
    }
    return render(request, "news/standard-formate.html", context)



def categories_list(request):
    categories = Category.objects.all()  
    return render(request, 'news/categories_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id) 
    return render(request, 'news/category_detail.html', {'category': category})