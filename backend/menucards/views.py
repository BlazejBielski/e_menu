from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from menucards.models import Dish
from menucards.serializers import DishSerializer


class DishesView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DishSerializer
    queryset = Dish.objects.all()


class DishItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
