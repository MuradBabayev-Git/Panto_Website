
from django.urls import path, re_path

from .views import about_us, all_products, best_selling_products, categories_list, categories, contact, contact_success, news_detail, index
from news import views  
# from news.views import about, contact, index

urlpatterns = [
    path("", index , name="index"),
    path("index", index),
    path("news_detail/<int:news_id>/", news_detail, name="news_detail"),
    path('categories/', views.categories_list, name='categories'), 
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('best-selling/', best_selling_products, name='best_selling'),
    path('products/all/', all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),



]