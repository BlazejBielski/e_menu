from rest_framework.serializers import ModelSerializer

from .models import MenuCard, Dish


class MenuCardSerializer(ModelSerializer):
    class Meta:
        model = MenuCard
        fields = ('id', 'name', 'description', 'date_of_add', 'date_of_actualisation')


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'date_of_add', 'date_of_actualisation', 'price', 'preparation_time',
                  'is_vegetarian', 'menu_cards')


class MenuCardsSerializer(ModelSerializer):
    class Meta:
        model = MenuCard
        fields = ('name', 'description')
