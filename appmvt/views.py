from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse ("inicio")

def post(request):
    return HttpResponse ("post")

def vista_editor(request):
    return HttpResponse ("editor")

def about(request):
    return HttpResponse("about")

def contacto(request):
    return HttpResponse("contacto")

def mensaje (request):
    return HttpResponse ("mensaje")
    