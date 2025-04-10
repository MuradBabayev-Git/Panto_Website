from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time_create", null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time_update", null=True)
    is_published = models.BooleanField(default=True, verbose_name="Status")
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Content", null=True)
    image = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Image", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time_create", null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time_update", null=True)
    is_published = models.BooleanField(default=True, verbose_name="Status", null=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name="newss")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"news_id": self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Ad")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=300, verbose_name="Ad")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.gender

class Author(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Cinsi")
    name = models.CharField(max_length=300, verbose_name="Ad")
    surname = models.CharField(max_length=300, verbose_name="Soyad")
    age  = models.PositiveIntegerField(verbose_name="Yaş")
    birthday = models.DateField(verbose_name="Doğum tarixi")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name

class Product(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=300, verbose_name="Ad")
    price = models.FloatField(verbose_name="Qiymət")
    tax_price = models.FloatField(blank=True, null=True, verbose_name="Tax qiymət")
    discount_price = models.FloatField(blank=True, null=True, verbose_name="Endirimli qiymət")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tag")
    status = models.BooleanField(default=True, verbose_name="Status")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarixi")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    def __str__(self):
        return self.name