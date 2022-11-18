from django.shortcuts import render, get_object_or_404
from .models import Area, Article, Categories
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.views.generic import TemplateView
# Create your views here.

def categories(request):
    return {'categories':Categories.objects.all()}

def area(request):
    return {'areas':Area.objects.all()}


def all_articles(request):
    article = Article.objects.all()
    return render(request, 'home.html', {'article':article})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article_detail.html', {'articles' : article},)




def categories_list(request, category_slug):
    categories = get_object_or_404(Categories, slug=category_slug)
    article = Article.objects.filter(Category=categories)
    return render(request, 'category.html', {'Category':categories, 'article':article})


def area_list(request, area_slug):
    Areas = get_object_or_404(Area, slug=area_slug)
    article = Article.objects.filter(Location=Areas)
    return render(request, 'area_list.html', {'Location':Areas, 'article':article})



class PostApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer

class PostApiDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer