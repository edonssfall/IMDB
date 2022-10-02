from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializer import MovieSerializer, Movies
from .models import Movie
from django.db.models import Q
from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class RecPagination(PageNumberPagination):
    page_size = 6


class MovieAPIList(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


class MovieDetailsAPI(APIView):

    def get(self, request, imdb_id):
        movie = Movie.objects.get(imdb_id=imdb_id)
        serializer = MovieSerializer(movie)
        #result = list()
        #for genre in movie.genres:
        #    serializer += MovieSerializer(Movie.objects.filter(Q(genres__contains='{' + genre + '}')).order_by('rank'))
        #serializer += MovieSerializer(result, many=True)
        return Response(serializer.data)


class MovieEditAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movies
    lookup_field = 'imdb_id'
    permission_classes = [IsAdminUser]


class MoviesRecAPI(ListAPIView):
    serializer_class = Movies
    pagination_class = RecPagination

    def get_queryset(self):
        genres = self.request.GET.getlist('genres', '')
        imdb_id = self.request.GET.get('title', '')
        result = list()
        for genre in genres:
            result += Movie.objects.exclude(imdb_id=imdb_id).filter(
                Q(genres__contains='{' + genre + '}')).order_by('rank')[:6]
        return result
