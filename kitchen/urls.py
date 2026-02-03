from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishTypeListView,
    CookListView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "kitchen"
