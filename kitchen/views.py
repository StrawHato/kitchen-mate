from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import DishType, Cook, Ingredient, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
    }

    return render(request, "kitchen/index.html", context)
