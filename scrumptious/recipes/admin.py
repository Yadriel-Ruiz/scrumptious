from django.contrib import admin
from recipes.models import Recipe, AddingSteps, Ingredient

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "id",
    ]

@admin.register(AddingSteps)
class AddingStepsAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "instruction",
        "id",
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "recipe",
    )