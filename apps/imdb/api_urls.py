from django.urls import path
from .views import MovieAPIList, MovieDetailsAPI, MoviesRecAPI, MovieEditAPI

app_name = 'apps.imdb'

urlpatterns = [
    path('movies/', MovieAPIList.as_view()),
    path('title/<slug:imdb_id>/', MovieDetailsAPI.as_view()),
    path('title/<slug:imdb_id>/edit', MovieEditAPI.as_view()),
    path('', MoviesRecAPI.as_view())
]