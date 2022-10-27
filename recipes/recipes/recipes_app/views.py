from django.shortcuts import render, redirect

from recipes.recipes_app.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.recipes_app.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'POST':
        recipe.delete()
        return redirect('home page')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
