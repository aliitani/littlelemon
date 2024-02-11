from django.urls import path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('book', views.Book.as_view(), name="book"),
    path('reservations/', views.Reservation.as_view(), name="reservations"),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu-items/<int:id>', views.SingleMenuItem.as_view(), name='menu-item'),
]