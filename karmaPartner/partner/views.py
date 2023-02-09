from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseNotFound

# Create your views here.
def home(request):
    return HttpResponse("Hello on my site")

def categories(request, catid):
    return HttpResponse(f'</h1>статьи по категориям</h1></p>{catid}</p>')

def pageNotFound(request,e):
    return HttpResponseNotFound("<h2>Page not found</h2>")

def badRequest(request):
    return HttpResponseBadRequest('<h1>Некоректный запрос</h1><h3>Страница не существует</h3>')




