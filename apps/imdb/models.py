from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Movie(models.Model):
    class TitleType(models.TextChoices):
        SHORT = "short", _("Short")
        MOVIE = "movie", _("Movie")

    imdb_id = models.CharField(_("IMDB id"), max_length=255, blank=True)
    title_type = models.CharField(_("Type of the title"), max_length=255, choices=TitleType.choices)
    name = models.CharField(_("Name"), max_length=255)
    is_adult = models.BooleanField(_("Is Adult"))
    year = models.DateField(_("Release Date"), null=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name=_("Genres"))
    poster_url = models.CharField(_('url_image'), max_length=255, null=True, blank=True)
    rating_imdb = models.DecimalField(_('Rating'), null=True, blank=True, max_digits=3, decimal_places=2)
    rank = models.IntegerField(_('Rank'), null=True, blank=True)

    def __str__(self):
        return self.imdb_id


class Person(models.Model):
    imdb_id = models.CharField(_("IMDB id"), max_length=255, blank=True)
    name = models.CharField(_("Name"), max_length=255)
    birth_year = models.DateField(_("Birth Year"), null=True)
    death_year = models.DateField(_("Death Year"), null=True)
    image_url = models.CharField(_("url_image"), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.imdb_id


class PersonMovie(models.Model):
    movie_id = models.ForeignKey(Movie, related_name='movie_id', on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, related_name='person_id', on_delete=models.PROTECT)
    order = models.IntegerField(_("Ordering"))
    job = models.CharField(_("Job"), max_length=255, null=True)
    characters = ArrayField(
        models.CharField(max_length=255),
        verbose_name=_("Characters"),
        null=True
    )
