from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)

from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    Film
)

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
    fields = ['titre', 'evaluation', 'genres', 'acteur', 'synopsis', 'trailer', 'posteur', 'commentaires']
    success_url = reverse_lazy('cinetix:film-list')