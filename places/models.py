from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название", unique=True)
    description_short = models.TextField(blank=True,
                                         verbose_name="Сокращенное описание")
    description_long = HTMLField(verbose_name="Полное описание", blank=True)
    lat = models.FloatField(default=0.0, verbose_name="Широта", blank=True)
    lon = models.FloatField(default=0.0, verbose_name="Долгота", blank=True)

    def __str__(self):
        return str(self.title)  # Convert title to string representation


class Image(models.Model):
    img = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name="images", verbose_name="Место")
    position = models.PositiveSmallIntegerField(verbose_name="Позиция фото",
                                                default=0,
                                                blank=True,
                                                db_index=True)


class Meta(object):
    ordering = ["position"]


def __str__(self):
    return f'{self.position}, {self.place}'
