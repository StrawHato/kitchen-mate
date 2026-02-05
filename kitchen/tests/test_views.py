from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.forms import (
    DishSearchForm, DishTypeSearchForm, IngredientSearchForm, CookSearchForm
)
from kitchen.models import DishType, Dish, Ingredient


class ViewTests(TestCase):
    fixtures = ["data.json"]

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admins_password",
        )
        self.client.force_login(self.admin_user)

    def test_dish_list_view_without_search_param(self):
        response = self.client.get(reverse("kitchen:dish-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["dish_list"])
        self.assertTrue(response.context["search_form"])
        self.assertTrue(response.context["is_paginated"])

    def test_dish_list_view_with_search_param(self):
        response = self.client.get(
            reverse("kitchen:dish-list"),
            data={"name": "salmon"}
        )
        all_dishes = Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.context["dish_list"][0]),
            "Grilled Salmon (price:12.00, dish_type:Main course)"
        )
        self.assertIsInstance(
            response.context["search_form"],
            DishSearchForm,
        )
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_list"]), 1)
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "salmon"
        )
        self.assertNotEqual(len(response.context["dish_list"]), all_dishes)

    def test_dish_type_list_view_without_search_param(self):
        response = self.client.get(reverse("kitchen:dish-types-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["dish_type_list"])
        self.assertTrue(response.context["search_form"])
        self.assertTrue(response.context["is_paginated"])

    def test_dish_type_list_view_with_search_param(self):
        response = self.client.get(
            reverse("kitchen:dish-types-list"),
            data={"name": "salad"}
        )
        all_dish_types = DishType.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.context["dish_type_list"][0]),
            "Salad"
        )
        self.assertIsInstance(
            response.context["search_form"],
            DishTypeSearchForm,
        )
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["dish_type_list"]), 1)
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "salad"
        )
        self.assertNotEqual(len(response.context["dish_type_list"]), all_dish_types)

    def test_ingredient_list_view_without_search_param(self):
        response = self.client.get(reverse("kitchen:ingredient-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["ingredient_list"])
        self.assertTrue(response.context["search_form"])
        self.assertTrue(response.context["is_paginated"])

    def test_ingredient_list_view_with_search_param(self):
        response = self.client.get(
            reverse("kitchen:ingredient-list"),
            data={"name": "onion"}
        )
        all_ingredients = Ingredient.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.context["ingredient_list"][0]),
            "Onion"
        )
        self.assertIsInstance(
            response.context["search_form"],
            IngredientSearchForm,
        )
        self.assertFalse(response.context["is_paginated"])
        self.assertEqual(len(response.context["ingredient_list"]), 1)
        self.assertEqual(
            response.context["search_form"].initial["name"],
            "onion"
        )
        self.assertNotEqual(len(response.context["ingredient_list"]), all_ingredients)

    def test_cook_list_view_without_search_param(self):
        response = self.client.get(reverse("kitchen:cook-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["cook_list"])
        self.assertTrue(response.context["search_form"])
        self.assertTrue(response.context["is_paginated"])

    def test_cook_list_view_with_search_param(self):
        response = self.client.get(
            reverse("kitchen:cook-list"),
            data={"username": "cook"}
        )
        all_cooks = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.context["cook_list"][0]),
            "cook1: John Doe"
        )
        self.assertIsInstance(
            response.context["search_form"],
            CookSearchForm,
        )
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["cook_list"]), 5)
        self.assertEqual(
            response.context["search_form"].initial["username"],
            "cook"
        )
        self.assertNotEqual(len(response.context["cook_list"]), all_cooks)
