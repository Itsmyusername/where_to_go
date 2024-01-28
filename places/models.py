from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=300)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(verbose_name='Полное описание')
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveSmallIntegerField(verbose_name='Позиция фото',
                                                default=0,
                                                blank=True)


    class Meta(object):
        ordering = ['position']


    def __str__(self):
        return f'{self.position}, {self.place}'
