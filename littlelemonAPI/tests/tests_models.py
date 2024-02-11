from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        expected_result = "IceCream : 80"
        actual_result = f"{item.title} : {item.price}"
        self.assertEqual(actual_result, expected_result)
        self.assertIsInstance(expected_result, str)