from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

class FilmListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Film
    template_name = 'cinetix/film/film_list.html'
    context_object_name = 'films'


class FilmCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Film
    fields = ['titre', 'evaluation', 'genres', 'acteur', 'synopsis', 'trailer', 'posteur', 'commentaires']
    success_url = reverse_lazy('cinetix:film-list')
    

class FilmUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Film
    pk_url_kwarg = 'id_film'
    fields = ['titre', 'evaluation', 'genres', 'acteur', 'synopsis', 'trailer', 'posteur', 'commentaires']
    success_url = reverse_lazy('cinetix:film-list')


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model =  Film
    pk_url_kwarg = 'id_film'
    success_url = reverse_lazy('cinetix:film-list')
    

class ProjListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Projection
    template_name = 'cinetix/projection/fc_list.html'
    context_object_name = 'projection'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectionForm()  # Ajouter le formulaire de création
        return context
    

class ProjCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Projection
    form_class = ProjectionForm
    template_name = 'cinetix/projection/proj_create.html'  # Votre template HTML pour ce formulaire
    success_url = reverse_lazy('cinetix:projection-list')  # Redirige vers la liste des projections après la soumission
