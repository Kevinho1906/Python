from django.shortcuts import render
from appTienda.models import Categoria
from appTienda.models import Producto
from django.db import Error

# Create your views here.

def inicio(request):
    return render(request, "listarProductos.html")

def vistaCategorias(request):
    return render(request, "frmAgregarCategoria.html")

def agregarCategoria(request):
    nombre = request.POST["txtCategoria"]
    try:
        
        categoria = Categoria(catNombre=nombre)
        categoria.save()
        mensaje = "Categoria Agregada Correctamente..."
        
    except Error as error:
        mensaje = f"Problemas al Agregar la Categoria {error}"
        
    retorno = {"mensaje":mensaje}
    return render(request, "frmAgregarCategoria.html", retorno)

def listarProductos(request):
    try:
        
        productos = Producto.objects.all()
        mensaje = ""
        
    except Error as error:
        mensaje = f"Problemas al Agregar la Categoria {error}"
        
    retorno = {"mensaje":mensaje, "listaProductos":productos}
    return render(request, "listarProductos.html", retorno)