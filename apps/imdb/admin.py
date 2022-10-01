from django.contrib import admin
from .models import Movie, Person


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'imdb_id', 'name')
