from django.contrib import admin
from .models import Categories, Area, Article


# Register your models here.
@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':['name',]}

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':['name']}



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {'slug':['title']}