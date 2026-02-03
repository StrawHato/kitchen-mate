from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cooks"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} (price:{self.price}, dish_type:{self.dish_type.name})"
