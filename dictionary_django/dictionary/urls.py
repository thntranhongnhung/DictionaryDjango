from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.vocabulary, name='vocabulary'),
    path('home/details/<int:id>', views.details, name='details')
]
