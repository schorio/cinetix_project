from django import forms

from .models import Film


class film_form(forms.ModelForm):


    class Meta:
        model = Film
        fields = [
            'titre', 'genres', 'acteur', 'synopsis',
            'evaluation', 'trailer', 'posteur', 'commentaires'      
        ]
        # widgets = {
        #     'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        #     'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        # }