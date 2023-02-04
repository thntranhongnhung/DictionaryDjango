from django.db import models
from django.urls import reverse
class dictionary(models.Model):
    word = models.SlugField(max_length=255)
    translate_word= models.CharField(max_length=255,null=True)
    des = models.CharField(max_length=255)
    example= models.CharField(max_length=255,null=True)
    language= models.CharField(max_length=255,null=True)

    slug = models.SlugField(default="",null=False)  # new

    def __str__(self):
        return f"{self.word} "

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})




