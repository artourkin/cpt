from Main.Logic.Controller import Controller

__author__ = 'artur'
from django.shortcuts import render


def home(request):
    context = {}
    controller = Controller()
    frequencies = controller.aggregate("mimetype")
    context.setdefault("mimetype", frequencies)
    template = "home.html"
    return render(request, template, context)