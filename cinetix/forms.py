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
        fields = ['film', 'type_proj', 'date_proj', 'heure_proj', 'paf_proj', 'desc_proj',  'place_proj']
        widgets = {
            'date_proj': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_proj': forms.TextInput(attrs={'class': 'form-control'}),
            'paf_proj': forms.TextInput(attrs={'class': 'form-control'}),
            'desc_proj': forms.TextInput(attrs={'class': 'form-control'}),
            'paf_proj': forms.TextInput(attrs={'class': 'form-control'}),
            'place_proj': forms.TextInput(attrs={'class': 'form-control'}),
        }
