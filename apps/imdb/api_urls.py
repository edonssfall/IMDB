from django.urls import path
from .views import MovieAPIList, MovieDetailsAPI, MoviesRecAPI, MovieEditAPI, PersonAPIList, PersonDetailsAPI, \
    PersonRecAPI, PersonEditAPI, search_api

app_name = 'apps.imdb'

urlpatterns = [
    path('movies/', MovieAPIList.as_view(),),
    path('movies/search', search_api),
    path('title/<slug:imdb_id>/', MovieDetailsAPI.as_view()),
    path('title/<slug:imdb_id>/edit/', MovieEditAPI.as_view()),
    path('titles/', MoviesRecAPI.as_view()),
    path('persons/', PersonAPIList.as_view()),
    path('name/<slug:imdb_id>/', PersonDetailsAPI.as_view()),
    path('name/<slug:imdb_id>/edit/', PersonEditAPI.as_view()),
    path('names/', PersonRecAPI.as_view())
]
