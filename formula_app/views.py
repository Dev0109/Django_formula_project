# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def formula(request):
    template = loader.get_template('formula.html')
    return HttpResponse(template.render())