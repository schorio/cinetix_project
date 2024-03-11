from django.views.generic import (
    ListView,
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
