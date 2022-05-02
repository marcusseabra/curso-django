from unicodedata import category

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Documentação: https://docs.djangoproject.com/en/4.0/topics/db/models/
class Category(models.Model):
    name = models.CharField(max_length=65)

    # Este 'método mágico' indica ao utilitário admin que deve ser exibido o campo retornado no grid que exibe a tabela
    def __str__(self):
        return self.name


class Recipe (models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # Deve-se configurar o settings.py para estabelecer a pasta (árvore de pasta) em que o arquivo será salvo
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
