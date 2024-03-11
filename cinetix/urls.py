from django.urls import path

from .views import (
    FilmListView,
)

urlpatterns = [
    path('film-list/', FilmListView.as_view(), name='film-list')
]
