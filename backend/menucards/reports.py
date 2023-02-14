import datetime
from abc import ABC

from django.db.models import Count, Transform

from .models import Dish
from django.db import models


class MySQLDatetimeDate(Transform, ABC):

    lookup_name = 'date'

    def as_sql(self, compiler, connection, **kwargs):
        lhs, params = compiler.compile(self.lhs)
        return 'DATE({})'.format(lhs), params

    @property
    def output_field(self):
        return models.DateField()


def dish_report():
    queryset = Dish.objects.values('menu_cards__name').annotate(
        count=Count('id')
    )

    return queryset


def dish_report_added_daily():
    daily_added = datetime.datetime.now() - datetime.timedelta(days=1)
    queryset = Dish.objects.filter(date_of_add__date__gte=daily_added)
    return queryset


def dish_report_changed_daily():
    daily_changed = datetime.datetime.now() - datetime.timedelta(days=1)
    queryset = Dish.objects.filter(date_of_actualisation__date__gte=daily_changed)
    return queryset
