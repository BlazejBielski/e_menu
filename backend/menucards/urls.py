from django.urls import path

from . import views


app_name = 'menucards'


urlpatterns = [
    path('dishes/', views.DishesView.as_view(), name='dishes'),
    path('dishes/<int:pk>/', views.DishItemView.as_view(), name='dish'),
    path('cards/', views.MenuCardsView.as_view(), name='cards'),
    path('cards/<int:pk>', views.MenuCardView.as_view(), name='card'),

]
