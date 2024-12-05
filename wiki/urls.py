from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wiki/<str:page_name>/', views.view_page, name='view_page'),
    path('wiki/<str:page_name>/edit/', views.edit_page, name='edit_page'),
]
