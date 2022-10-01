from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import MovieSerializer, Movies
from .models import Movie
from django.db.models import Q


class MovieAPIList(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


class MovieDetailsAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    lookup_field = 'imdb_id'

    def get_queryset(self):
        return Movie.objects.all()


class MoviesRecAPI(ListCreateAPIView):
    serializer_class = Movies
    lookup_field = 'genres'

    def get_queryset(self):
        return Movie.objects.filter(Q(genres__contains='{Drama}') | Q(genres__contains='{}')).order_by('rank')