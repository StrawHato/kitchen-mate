from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Ingredient, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price", "description")
    list_filter = ("dish_type",)
    search_fields = ("name",)

@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("first_name", "last_name", "years_of_experience",)}
        ),
    )
    list_filter = UserAdmin.list_filter
    search_fields = UserAdmin.search_fields


admin.site.register(DishType)
admin.site.register(Ingredient)
