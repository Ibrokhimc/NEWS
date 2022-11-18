from django.urls import path

from . import views
from .views import PostApiView, PostApiDetail

app_name = 'page'
urlpatterns = [
    path('', views.all_articles, name='home'),
    path('pages/<slug:slug>/', views.article_detail, name='article_detail'),
    path('search/<slug:category_slug>/', views.categories_list, name='category_list'),
    path('hududlar/<slug:area_slug>/', views.area_list, name='area_list'),
    path('api', PostApiView.as_view(), name='api'),
    path('api_detail', PostApiDetail.as_view(), name='api_detail')

]
