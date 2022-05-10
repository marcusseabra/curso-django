from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.recipe.factory import make_recipe

from recipes.models import Recipe


# Create your views here.
def home(request):
    # recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    recipes = []
    # O campo context é passado como parâmetro para a página de modo que a página enxerga o conteúdo da variável.
    # No caso abaixo, trata-se de uma lista chamada recipes. A lista contém dicionários capturados na base de dados
    return render(request, "recipes/pages/home.html", context={
        "recipes": recipes})


def category(request, category_id):
    # Busca pelas receitas com base na categoria enviada no contexto e filtrada no model
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by("-id")

#    if not recipes:
#        raise Http404("Page not found")

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id,
                              is_published=True).order_by("-id"))

    return render(request, "recipes/pages/category.html", context={
        "recipes": recipes,
        "title": f'{recipes[0].category.name}'})


def recipe(request, recipe_id):

    recipe = get_object_or_404(Recipe, id=recipe_id, is_published=True)

    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": recipe,
        "is_detail_page": True})
