from pstats import Stats
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from transliterate import translit


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Tabels.Status.PUBLISHED)

class Tabels(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    name = models.CharField(max_length=25)
    played = models.CharField(max_length=25)  
    won = models.CharField(max_length=255)
    drawn = models.CharField(max_length=255)
    lost = models.CharField(max_length=255)
    fors = models.CharField(max_length=255, default='default_value')
    against = models.CharField(max_length=255)
    goal_difference = models.CharField(max_length=255)
    points =models.CharField(max_length=255)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    
    
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.name