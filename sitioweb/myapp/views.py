from cgi import test
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import familia

def lista_familia(request):
    queryset = familia.objects.all()
    diccionario = {'familia' : queryset}
    plantilla = loader.get_template('lista_familia.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)
