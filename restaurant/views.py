from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views import View
from django.http import Http404, HttpResponse

from datetime import datetime
import json

from littlelemonAPI.serializers  import BookingSerializer, MenuItemSerializer
from littlelemonAPI.models import Booking, Menu as MenuModel

from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'index.html');

def about(request):
    return render(request, 'about.html')

class Book(View):
    template_name = 'book.html'

    def post(self, request):
        form = BookingForm(request.POST)
        print(form.data)
        return HttpResponse('content')
    
    def get(self, request):
        bookings = Booking.objects.all()
        booking_serializer = BookingSerializer(data=bookings.values(), many=True)
        booking_serializer.is_valid()
        
        form = BookingForm()
        return render(request, self.template_name, {'form': form, 'bookings': booking_serializer.data, 'bookingDate': datetime.now().date()})
    
        

class Reservation(View):
    template_name = 'reservations.html'

    def get(self, request):
        bookings = Booking.objects.all()
        booking_json = BookingSerializer(data=bookings, many=True)
        booking_json.is_valid()

        return render(request, self.template_name, {"bookings": json.dumps(booking_json.data)})

class Menu(View):
    template_name = 'menu.html'

    def get(self, request):
        menu = MenuModel.objects.all()
        menu_json = MenuItemSerializer(menu, many=True).data
        return render(request, self.template_name, {"menu": menu_json}) 

class SingleMenuItem(DetailView):
    model = MenuModel.objects.all()
    template_name = 'menu_item.html'
    
    def get(self, request, id=None):
        try:
            menu_item = MenuModel.objects.get(id=id)    
            menu_item_json = MenuItemSerializer(menu_item).data
        except MenuModel.DoesNotExist:
            raise Http404('Id DOES NOT EXIST')
            
        return render(request, self.template_name, {"menu_item": menu_item_json})
        