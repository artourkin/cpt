from Main.Logic.Controller import Controller

__author__ = 'artur'
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    controller = Controller()
    frequencies = controller.aggregate("mimetype")
    context.setdefault("mimetype", frequencies)
    template = "home.html"
    return render(request, template, context)

def mimetype(request):
    controller = Controller()
    frequencies = controller.aggregate("mimetype")
    return HttpResponse(frequencies.__str__())

def format(request):
    controller = Controller()
    frequencies = controller.aggregate("format")
    return HttpResponse(frequencies.__str__())