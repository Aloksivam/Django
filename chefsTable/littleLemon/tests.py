from django.test import TestCase
from .models import Menu
from datetime import datetime

class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu=Menu.objects.create(
            name='samosa',
            cuisine=' bihari',
            fee=344
        )
    def test_fields(self):
        self.assertIsInstance(self.menu.name,str)
        self.assertIsInstance(self.menu.cuisine,str)
        self.assertIsInstance(self.menu.fee,int)
# Create your tests here.
