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
        fields = [
            'name',
            'imdb_id',
            'image_url',
            'birth_place'
        ]


class PersonsMovie(serializers.ModelSerializer):
    person_id = Persons()
    movie_id = Movies()

    class Meta:
        model = PersonMovie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    movie_id = PersonsMovie(many=True, read_only=True)

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
            'get_absolute_url'
        ]


class MovieEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'rating_imdb',
            'imdb_id',
            'name',
            'year',
            'poster_url',
            'rank'
        ]


class PersonSerializer(serializers.ModelSerializer):
    person_id = PersonsMovie(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class PersonEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = [
            'name',
            'birth_year',
            'death_year',
            'birth_place',
            'image_url'
        ]
