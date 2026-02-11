from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Ingredient, Dish


class ModelsTest(TestCase):
    fixtures = ["data.json"]

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(pk=1)
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_str(self):
        dish = Dish.objects.get(pk=1)
        self.assertEqual(
            str(dish),
            f"{dish.name} (price:{dish.price}, dish_type:{dish.dish_type.name})"
        )

    def test_cook_str(self):
        cook = get_user_model().objects.get(pk=1)
        self.assertEqual(
            str(cook),
            f"{cook.username}: {cook.first_name} {cook.last_name}"
        )

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.get(pk=1)
        self.assertEqual(str(ingredient), ingredient.name)

    def test_get_absolute_url_cook(self):
        cook = get_user_model().objects.get(pk=1)
        self.assertEqual(
            cook.get_absolute_url(),
            reverse("kitchen:cook-detail", args=[cook.id])
        )

    def test_get_absolute_url_dish(self):
        dish = Dish.objects.get(pk=1)
        self.assertEqual(
            dish.get_absolute_url(),
            reverse("kitchen:dish-detail", args=[dish.id])
        )
