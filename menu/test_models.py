from django.test import TestCase
from .models import Menu


class TestMenuModel(TestCase):
    def setUp(self):

        self.food_item = Menu.objects.create(
            name="Burger",
            description ="Amazing burger!",
            category="food",
            image="placeholder"
        )
        self.drink_item = Menu.objects.create(
            name="Coke",
            description="Soft drink",
            category="drink",
            image="placeholder"
        )
    
    def test_menu_str_returns_name(self):
        self.assertEqual(str(self.food_item), "Burger")
        self.assertEqual(str(self.drink_item), "Coke")


    def test_menu_category_choices(self):
        self.assertIn(self.food_item.category, dict(Menu.CATEGORY_CHOICES))
        self.assertIn(self.drink_item.category, dict(Menu.CATEGORY_CHOICES))
