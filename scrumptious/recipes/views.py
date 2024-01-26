from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Recipe
from recipes.forms import RecipeForm, EditForm
from django.contrib.auth.decorators import login_required

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id = id)
    context = {
        "recipe": recipe,
    }
    return render(request, "recipes/detail.html", context)

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe": recipes,
    }
    return render(request, "recipes/list.html", context)
# recipes/templates/recipes

@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("home")
    else:
        form = RecipeForm()
    context = {
        "form": form
    }
    return render(request, "recipes/create.html", context)

@login_required
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id) 
    else:
        form = RecipeForm(instance=recipe)

    context = {
        "editform": form,
        "recipe": recipe,
    }
    return render(request, "recipes/edit.html", context)

@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        "recipe": recipes,
    }
    return render(request, "recipes/list.html", context)