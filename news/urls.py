
from django.urls import path, re_path

from .views import categories_list, categories, news_detail, index
# from news.views import about, contact, index

urlpatterns = [
    path("", index , name="index"),
    path("index", index),
    path("category/<int:cat_id>/", categories ,  name="category"),
    path('categories/', categories_list, name='categories'),
    path("news/<int:news_id>/", news_detail ,  name="news_detail"),
]

