from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)
    no_of_guests = models.IntegerField(default=1)
    
    def __str__(self): 
        return self.name

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')
        
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_item_description = models.TextField(max_length=1000, default='')
    inventory = models.IntegerField()
    
    def __str__(self): 
        return f'{self.title} : {str(self.inventory)}'
    