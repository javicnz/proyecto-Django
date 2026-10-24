from django.shortcuts import render

from saludo.application.services.saludar_service import SaludarService


def home(request):
    return render(request, "hello.html", {"greeting": SaludarService().ejecutar()})