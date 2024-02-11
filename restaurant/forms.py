from django.forms import ModelForm, TimeField, Select
from littlelemonAPI.models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        
    reservation_slot = TimeField(
        widget= Select(choices=[(f"{hour:02}:00", f"{hour:02}:00") for hour in range(10, 21)]),
        label='Reservation Slot'
    )
        
