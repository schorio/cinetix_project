from django import forms
from .models import Projection, Film

class ProjectionForm(forms.ModelForm):
    film = forms.ModelChoiceField(
        queryset=Film.objects.all(),
        empty_label="Choisir un film",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    type_proj = forms.ChoiceField(
        choices=[
            ('FC', 'Film Complet'),
            ('FAP', 'Avant-Première'),
            ('FP', 'Prochainement'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Projection
        fields = ['film', 'type_proj', 'date', 'heure', 'description', 'paf']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'paf': forms.TextInput(attrs={'class': 'form-control'}),
        }
