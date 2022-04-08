from django.urls import path

from recipes.views import about, contacts, my_view

urlpatterns = [
    path('', my_view),
    path('sobre/', about),
    path('contatos/', contacts),
]
