from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from .serializer import MovieSerializer, Movies
from .models import Movie
from django.db.models import Q
from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class MovieFilter(filters.FilterSet):
    genres = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['genres']


class RecPagination(PageNumberPagination):
    page_size = 6


class MovieAPIList(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


class MovieDetailsAPI(RetrieveAPIView):
    serializer_class = MovieSerializer
    lookup_field = 'imdb_id'

    def get_queryset(self):
        return Movie.objects.all()


class MovieEditAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'imdb_id'

class MoviesRecAPI(ListAPIView):
    serializer_class = Movies
    filterset_class = MovieFilter
    pagination_class = RecPagination

    def get_queryset(self):
        req = self.request.GET.getlist('genres', '')
        if len(req) == 1:
            return Movie.objects.filter(
                Q(genres__contains='{' + req[0] + '}')
            ).order_by('rank')
        elif len(req) == 2:
            return Movie.objects.filter(
                Q(genres__contains='{' + req[0] + '}') |
                Q(genres__contains='{' + req[1] + '}')
            ).order_by('rank')
        elif len(req) == 3:
            return Movie.objects.filter(
                Q(genres__contains='{' + req[0] + '}') |
                Q(genres__contains='{' + req[1] + '}') |
                Q(genres__contains='{' + req[2] + '}')
            ).order_by('rank')
        else:
            return Http404
