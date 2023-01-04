from django.contrib import admin
from .models import dictionary
admin.site.register(dictionary)
class DictionsryAdmin(admin.ModelAdmin):
    list_display = ("word")

admin.site.register(dictionary,DictionsryAdmin)