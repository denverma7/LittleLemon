from django.test import TestCase
from LittleLemonAPI.models import MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        menu_item = MenuItem.objects.create(Title='Pizza', Price=10.99, Inventory=5)
        # self.assertEqual(menu_item.get_item(), 'Pizza : 10.99')
        self.assertEqual(str(menu_item), "Pizza: 10.99")