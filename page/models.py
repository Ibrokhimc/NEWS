from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta():
        verbose_name_plural = 'categories'


    def get_absolute_url(self):
        return reverse('page:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name
    class Meta():
        verbose_name_plural = 'areas'


    def get_absolute_url(self):
        return reverse('page:area_list', args=[self.slug])

class Article(models.Model):
    Category = models.ForeignKey(Categories, related_name='category', on_delete=models.CASCADE)
    Location = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=250)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    class Meta():
        verbose_name_plural = 'Article_list'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('page:article_detail', args=[self.slug])
