import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from LittleLemonAPI.models import Menu, MenuItem
from LittleLemonAPI.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        """Add a few test instances of the Menu model"""
        self.menu1 = Menu.objects.create(Title='Burger', Price=10.99, Inventory=5)
        self.menu2 = Menu.objects.create(Title='Pizza', Price=20.99, Inventory=10)
        self.menu3 = Menu.objects.create(Title='Pasta', Price=15.50, Inventory=8)
        self.client = Client()

    def test_getall(self):
        """Test retrieving all Menu objects and verify serialized data"""
        # Retrieve all Menu objects
        all_menus = Menu.objects.all()
        
        # Serialize the data
        serialized_data = MenuSerializer(all_menus, many=True).data
        
        # Verify that we have 3 menu items
        self.assertEqual(len(serialized_data), 3)
        
        # Verify the serialized data matches the created objects
        self.assertEqual(serialized_data[0]['Title'], 'Burger')
        self.assertEqual(serialized_data[0]['Price'], '10.99')
        self.assertEqual(serialized_data[0]['Inventory'], 5)
        
        self.assertEqual(serialized_data[1]['Title'], 'Pizza')
        self.assertEqual(serialized_data[1]['Price'], '20.99')
        self.assertEqual(serialized_data[1]['Inventory'], 10)
        
        self.assertEqual(serialized_data[2]['Title'], 'Pasta')
        self.assertEqual(serialized_data[2]['Price'], '15.50')
        self.assertEqual(serialized_data[2]['Inventory'], 8)


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=User.objects.create_user(username='tester'))

    def test_inventory_update_persists(self):
        menu_item = MenuItem.objects.create(Title='Pizza', Price=10.99, Inventory=5)

        response = self.client.patch(
            f'/api/menu-items/{menu_item.ID}',
            data=json.dumps({'Inventory': 2}),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(MenuItem.objects.get(ID=menu_item.ID).Inventory, 2)