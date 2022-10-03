from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializer import MovieSerializer, Movies, MovieEditSerializer
from .models import Movie
from django.db.models import Q
from rest_framework.response import Response


class MovieAPIList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDetailsAPI(APIView):

    def get(self, request, imdb_id):
        movie = Movie.objects.get(imdb_id=imdb_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class MovieEditAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieEditSerializer
    lookup_field = 'imdb_id'


class MoviesRecAPI(ListAPIView):
    serializer_class = Movies

    def get_queryset(self):
        genres = self.request.GET.getlist('genres', '')
        imdb_id = self.request.GET.get('title', '')
        result = list()
        for genre in genres:
            result += Movie.objects.exclude(imdb_id=imdb_id).filter(
                Q(genres__contains='{' + genre + '}')).order_by('rank')[:6]
        return result[:6]
