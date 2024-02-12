from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from datetime import datetime

from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.

class MenuItemAPIView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingAPIView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        reservation_date = self.request.query_params.get('date', datetime.today().date())    
        self.queryset = self.queryset.filter(reservation_date=reservation_date)

        return super().get(request, *args, **kwargs)
    
class SingleMenuItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
