from django.db import models

class dictionary(models.Model):
    word = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    example= models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.word} "
 