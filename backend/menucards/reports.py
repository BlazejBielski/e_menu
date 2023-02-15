from datetime import timedelta
from django.utils import timezone

from django.db.models import Count

from .models import Dish


def dish_report():
    queryset = Dish.objects.values('menu_cards__name').annotate(
        count=Count('id')
    )
    return queryset


def dish_report_added_daily():
    daily_added = timezone.now() - timedelta(days=1)
    queryset = Dish.objects.filter(date_of_add__gte=daily_added)
    return queryset


def dish_report_changed_daily():
    daily_changed = timezone.now() - timedelta(days=1)
    queryset = Dish.objects.filter(date_of_actualisation__gte=daily_changed)
    return queryset
