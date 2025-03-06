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
