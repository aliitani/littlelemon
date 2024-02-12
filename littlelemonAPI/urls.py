from django.urls import path, include
from . import views

app_name = 'littlelemonAPI'

urlpatterns = [
    path('menu/', views.MenuItemAPIView.as_view(), name='menu-api'),
    path('menu-items/<int:pk>/', views.SingleMenuItemAPIView.as_view(), name='menu-items-api'),
    path('bookings/', views.BookingAPIView.as_view(), name="bookings-api")
]