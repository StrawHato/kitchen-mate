from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishTypeListView,
    CookListView,
    IngredientListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientCreateView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
]

app_name = "kitchen"
