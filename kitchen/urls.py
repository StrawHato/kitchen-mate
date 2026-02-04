from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    CookListView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
]

app_name = "kitchen"
