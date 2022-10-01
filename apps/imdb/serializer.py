from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import serializers
from .models import Movie, Person, PersonMovie


class MyPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class Movies(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class Persons(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name']


class PersonsMovie(serializers.ModelSerializer):
    person_id = Persons()

    class Meta:
        model = PersonMovie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    movie_id = PersonsMovie(many=True)

    class Meta:
        model = Movie
        fields = [
            'rating_imdb',
            'imdb_id',
            'name',
            'year',
            'genres',
            'poster_url',
            'rank',
            'movie_id',
        ]
