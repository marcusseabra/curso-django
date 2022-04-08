from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    retorno_pagina = "Olá Django. Aqui devem vir páginas web como \
        respostas às requisições!"
    return HttpResponse(retorno_pagina)


def contacts(request):
    retorno_pagina = "Página de contatos"
    return HttpResponse(retorno_pagina)


def about(request):
    retorno_pagina = "Sobre a minha página"
    return HttpResponse(retorno_pagina)
