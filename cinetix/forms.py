from django import forms
from .models import Film

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ['titre', 'evaluation', 'genres', 'acteur', 'synopsis', 'trailer', 'posteur', 'commentaires']
