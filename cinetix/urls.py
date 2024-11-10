from django.urls import path

from .views import *

app_name = "cinetix"

urlpatterns = [
    path('film-list/', FilmListView.as_view(), name='film-list'),
    path('film-list/nouveau/', FilmCreateView.as_view(), name='film-create'),
    path('film-list/<str:id_film>/modification/', FilmUpdateView.as_view(), name='film-update'),
    path('film-list/<str:id_film>/suppresion/', FilmDeleteView.as_view(), name='film-delete'),
    path('projection-list/', ProjListView.as_view(), name='projection-list'),
    path('projection-list/nouveau/', ProjCreateView.as_view(), name='projection-create'),
]
