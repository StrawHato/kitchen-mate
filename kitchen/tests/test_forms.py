from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.forms import (
    CookCreationForm,
    CookExperienceUpdateForm,
    DishTypeSearchForm,
    DishSearchForm,
    IngredientSearchForm,
    CookSearchForm,
)


class FormsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = get_user_model().objects.create_superuser(
            username="admin",
            password="test_password",
        )
        self.client.force_login(self.superuser)

    def test_cook_creation_form_with_valid_first_last_name_experience(self):
        form_data = {
            "username": "user",
            "password1": "user12565password",
            "password2": "user12565password",
            "first_name": "John",
            "last_name": "Smith",
            "years_of_experience": 2,
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"], form_data["last_name"])
        self.assertEqual(
            form.cleaned_data["years_of_experience"],
            form_data["years_of_experience"]
        )

    def test_cook_creation_form_with_invalid_first_last_name_experience(self):
        form_data = {
            "username": "user",
            "password1": "user12565password",
            "password2": "user12565password",
            "first_name": "John",
            "last_name": "Smith",
            "years_of_experience": 101,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_cook_creation_form_contains_years_of_experience_first_last_name_fields(self):
        url = reverse("kitchen:cook-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "years_of_experience")
        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")

    def test_cook_experience_update_form(self):
        cook = get_user_model().objects.create_user(
            username="user",
            password="password1212",
            years_of_experience=2,
        )

        form = CookExperienceUpdateForm(
            data={"years_of_experience": 5},
            instance=cook,
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["years_of_experience"], 5)

    def test_dish_type_search_form_with_empty_query_param(self):
        form = DishTypeSearchForm(
            data={"name": ""}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
        self.assertTrue(form.fields["name"].label is None or form.fields["name"].label == "")

    def test_dish_type_search_form_with_query_param(self):
        form = DishTypeSearchForm(
            data={"name": "a"}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "a")

    def test_dish_search_form_with_empty_query_param(self):
        form = DishSearchForm(
            data={"name": ""}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
        self.assertTrue(form.fields["name"].label is None or form.fields["name"].label == "")

    def test_dish_search_form_with_query_param(self):
        form = DishSearchForm(
            data={"name": "cake"}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "cake")

    def test_ingredient_search_form_with_empty_query_param(self):
        form = IngredientSearchForm(
            data={"name": ""}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
        self.assertTrue(form.fields["name"].label is None or form.fields["name"].label == "")

    def test_ingredient_search_form_with_query_param(self):
        form = IngredientSearchForm(
            data={"name": "butter"}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "butter")

    def test_cook_search_form_with_empty_query_param(self):
        form = CookSearchForm(
            data={"username": ""}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")
        self.assertTrue(form.fields["username"].label is None or form.fields["username"].label == "")

    def test_cook_search_form_with_query_param(self):
        form = CookSearchForm(
            data={"username": "admin"}
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "admin")
