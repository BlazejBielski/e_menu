from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from menucards.models import Dish, MenuCard
from menucards.serializers import DishSerializer, MenuCardSerializer


class DishesView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class DishItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class MenuCardsView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MenuCardSerializer
    queryset = MenuCard.objects.all()


class MenuCardView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuCardSerializer
    queryset = MenuCard.objects.all()
