from django.db import models

class dictionary(models.Model):
    word = models.SlugField(max_length=255)
    des = models.CharField(max_length=255)
    example= models.CharField(max_length=255,null=True)


    def __str__(self):
        return f"{self.word} "
 

class Layout(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="gallery",null=True, blank=True)
    def __str__(self):
        return f"{self.name} "
    def get_img_url(self):
        return self.image.url


