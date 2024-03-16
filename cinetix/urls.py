from django.urls import path

from .views import (
    FilmListView,
    FilmCreateView,
    FilmUpdateView
)

app_name = "cinetix"

urlpatterns = [
    path('film-list/', FilmListView.as_view(), name='film-list'),
    path('film-list/nouveau/', FilmCreateView.as_view(), name='film-create'),
    path('film-list/<int:pk>/modification/', FilmUpdateView.as_view(), name='film-update')
]
