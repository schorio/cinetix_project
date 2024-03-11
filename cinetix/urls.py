from django.urls import path

from .views import (
    FilmListView,
)

app_name = "cinetix"

urlpatterns = [
    path('film-list/', FilmListView.as_view(), name='film-list')
]
