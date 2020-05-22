from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    genres = models.CharField(max_length=500)

    def __str__(self):
        return self.title