from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishTypeListView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("types/", DishTypeListView.as_view(), name="dish-types-list"),
]

app_name = "kitchen"
