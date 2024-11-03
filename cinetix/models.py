from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Film(models.Model):
    id_film = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    genres = ArrayField(
        models.CharField(max_length=50),
        size=3,
        blank=True,
        default=list,
    )
    acteur = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=255)
    evaluation = models.FloatField()
    trailer = models.FileField(upload_to='static/video/trailer')
    posteur = models.ImageField(upload_to='static/img/film/')
    commentaires = models.CharField(max_length=255)
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('film-list')
    
    
    
class Projection(models.Model):
    id_proj = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="projections")
    type_proj = models.CharField(max_length=255)
    timings = models.CharField(max_length=255)
    place_proj = ArrayField(
        models.CharField(max_length=5),
        size=92,  # Taille maximale du tableau
        blank=True,
        default=list,  # Valeur par défaut pour le champ
    )
    paf = models.FloatField()
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.film