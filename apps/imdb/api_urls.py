from django.urls import path
from .views import MovieAPIList, MovieDetailsAPI, MoviesRecAPI

app_name = 'apps.imdb'

urlpatterns = [
    path('movies/', MovieAPIList.as_view()),
    path('title/<str:imdb_id>/', MovieDetailsAPI.as_view()),
    path('', MoviesRecAPI.as_view())
]