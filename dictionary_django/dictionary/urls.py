from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from dictionary import views
urlpatterns = [
     path('testing/', views.testing, name='testing'),
    path('home/', views.home, name='home'),
    path('home/vocabulary/', views.vocabulary, name='vocabulary'),
    path('home/vocabulary/details/<str:word>', views.details, name='details'),
    path('home/search', views.search, name='search')
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)