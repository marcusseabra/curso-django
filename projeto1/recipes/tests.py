from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, 'Um é igual a um'

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:nome')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={"category_id": 2})
        self.assertEqual(url, '/recipes/category/2/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', args=(2,))
        self.assertEqual(url, '/recipes/2/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:nome'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'recipe_id': 1})
        )
        self.assertIs(view.func, views.recipe)
