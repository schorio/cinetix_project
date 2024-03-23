from django.db import models
from django.urls import reverse

class Film(models.Model):
    titre = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    acteur = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    evaluation = models.FloatField()
    trailer = models.CharField(max_length=255)
    posteur = models.ImageField(upload_to='static/img/film/')
    commentaires = models.CharField(max_length=255)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('film-list')