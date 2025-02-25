from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

# defines url paths for the different views
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<slug:slug>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]