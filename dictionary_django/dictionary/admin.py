from django.contrib import admin
from .models import dictionary


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ("word",)

admin.site.register(dictionary,DictionaryAdmin)


