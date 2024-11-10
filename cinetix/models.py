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
    type_proj = models.CharField(max_length=20, choices=[
        ('FC', 'Film Complet'),
        ('FAP', 'Avant-Première'),
        ('FP', 'Prochainement'),
    ])
    date = models.CharField(max_length=255)
    heure = models.CharField(max_length=255)
    paf = models.FloatField()
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.film.titre