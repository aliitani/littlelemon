from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Menu
from ..serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=12, inventory=50)
        Menu.objects.create(title="Burger", price=15, inventory=30)

    def test_getall(self):
        user = User.objects.create_user(username='testuser', password='testpass')

        client = APIClient()
        client.force_authenticate(user)
        url = reverse('littlelemonAPI:menu-api')

        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)