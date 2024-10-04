from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contactos(request):
    return render(request, "contactos.html")

def empleados(request):
    return render(request, "empleados.html")

def clientes(request):
    return render(request, "clientes.html")

def productos(request):
    return render(request, "productos.html")

def ordenes(request):
    return render(request, "ordenes.html")

def proveedores(request):
    return render(request, "proveedores.html")

