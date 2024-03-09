from django.db import models
from django.urls import reverse

class Film(models.Model):
    titre = models.CharField(max_length=255, unique=True)
    categorie = models.CharField(max_length=255, unique=True)
    synopsis = models.CharField(max_length=255, unique=True)
    acteur = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('film-list')