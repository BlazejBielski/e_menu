from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Subquery

from menucards.models import Dish, MenuCard
from menucards.serializers import DishSerializer, MenuCardSerializer, MenuCardsSerializer


class DishesView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class DishItemView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class MenuCardsView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MenuCardSerializer
    queryset = MenuCard.objects.all()


class MenuCardView(RetrieveUpdateDestroyAPIView):
<<<<<<< HEAD
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MenuCardSerializer
=======
    serializer_class = MenuCardsSerializer
>>>>>>> EM-009_redis_and_celery_installation
    queryset = MenuCard.objects.all()
