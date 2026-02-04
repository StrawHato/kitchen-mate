from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishTypeListView,
    CookListView,
    IngredientListView,
    DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
]

app_name = "kitchen"
