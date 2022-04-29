from django.shortcuts import render
from utils.recipe.factory import make_recipe


# Create your views here.
def home(request):
    # O campo context é passado como parâmetro para a página de modo que a página enxerga o conteúdo da variável.
    # No caso abaixo, trata-se de uma lista chamada recipes. A lista contém dicionários criados pelo médodo make_recipe
    return render(request, "recipes/pages/home.html", context={
        "recipes": [make_recipe() for _ in range(4)]})


def recipe(request, id):
    return render(request, "recipes/pages/recipe-view.html", context={
        "recipe": make_recipe(),
        "is_detail_page": True})
