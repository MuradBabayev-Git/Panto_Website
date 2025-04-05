
from django.urls import path, re_path

from .views import categories_list, categories, news_detail, index
from news import views
# from news.views import about, contact, index

urlpatterns = [
    path("", index , name="index"),
    path("index", index),
    path("news/<int:news_id>/", news_detail ,  name="news_detail"),
    path('categories/', views.categories_list, name='categories'), 
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]