from atexit import register

from django.contrib import admin

from .models import Category, Recipe


# Definição das entidades que serão visíveis ao administrador
# A classe herda de ModelAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
