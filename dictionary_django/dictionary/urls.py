from django.urls import path
from . import views

urlpatterns = [
     path('testing/', views.testing, name='testing'),
    path('home/', views.home, name='home'),
    path('home/vocabulary/', views.vocabulary, name='vocabulary'),
    path('home/vocabulary/details/<str:word>', views.details, name='details')
]
