from django.urls import path
from . import views

urlpatterns = [
    path('twain/', views.twain, name='twain'),
    path('remarque/', views.remarque, name='remarque'),
    path('tolstoi/', views.tolstoi, name='tolstoi'),
    path('', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
]
