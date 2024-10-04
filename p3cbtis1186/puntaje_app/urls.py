from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("contactos/", views.contactos, name = "contactos"),
    path("empleados/", views.empleados, name = "empleados"),
    path("clientes/", views.clientes, name = "clientes"),
    path("productos/", views.productos, name = "productos"),
    path("ordenes/", views.ordenes, name = "ordenes"),
    path("proveedores/", views.proveedores, name = "proveedores"),
]