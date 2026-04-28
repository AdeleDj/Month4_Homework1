from django.urls import path
from . import views

urlpatterns = [
    path('twain/', views.twain, name='twain'),
    path('remarque/', views.remarque, name='remarque'),
    path('tolstoi/', views.tolstoi, name='tolstoi'),
]
