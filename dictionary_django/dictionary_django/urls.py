from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('dictionary.urls')),
    path('admin/', admin.site.urls),
]

