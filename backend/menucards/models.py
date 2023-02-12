from django.utils import timezone

from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    date_of_add = models.DateTimeField(auto_now_add=True)
    date_of_actualisation = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class MenuCard(Feature):
    pass


class Dish(Feature):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.DurationField()
    is_vegetarian = models.BooleanField(default=False)
    menu_cards = models.ManyToManyField('MenuCard', related_name='%(class)s')
