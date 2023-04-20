from django.shortcuts import render, redirect
from appTienda.models import Categoria
from appTienda.models import Producto
from django.db import Error

# Create your views here.

def inicio(request):
    return render(request, "listarProductos.html")

def vistaCategorias(request):
    try:
        
        productos = Categoria.objects.all()
        mensaje = ""
        
    except Error as error:
        mensaje = f"Problemas al Obtener las Categorias {error}"
        
    retorno = {"mensaje":mensaje, "listaCategorias":productos}
    return render(request, "frmAgregarCategoria.html", retorno)

def agregarCategorias(request):
    nombre = request.POST["txtCategoria"]
    try:
        
        categoria = Categoria(catNombre=nombre)
        categoria.save()
        mensaje = "Categoria Agregada Correctamente..."
        
    except Error as error:
        mensaje = f"Problemas al Agregar la Categoria {error}"
        
    retorno = {"mensaje":mensaje, "listaCategorias":Categoria.objects.all()}
    return render(request, "frmAgregarCategoria.html", retorno)

def listarProductos(request):
    try:
        
        productos = Producto.objects.all()
        mensaje = ""
        
    except Error as error:
        mensaje = f"Problemas al Obtener los Productos {error}"
        
    retorno = {"mensaje":mensaje, "listaProductos":productos}
    return render(request, "listarProductos.html", retorno)

def vistaProductos(request):
    try:
        categorias = Categoria.objects.all()
        mensaje = ""
    
    except Error as error:
        mensaje = f"Problemas al Obtener la Categoria {error}"
    
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "persona":None}
    return render(request, "frmAgregarProducto.html", retorno)
    
def agregarProducto(request):
    
    codigo = int(request.POST["txtCodigo"])
    nombre = request.POST["txtNombre"]
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES["fileFoto"]
    
    try:
        
        categoria = Categoria.objects.get(id=idCategoria)
        producto = Producto(proCodigo = codigo, proNombre = nombre, proPrecio = precio, proCategoria = categoria, proFoto = archivo)
        producto.save()
        mensaje = "Producto Agregado Correctamente..."
        
        return redirect("/listarProductos/")
    except Error as error:
        mensaje = f"Problemas al Agregar el Producto {error}"
        
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "producto":producto}

    return render(request, "frmAgregarProducto.html", retorno)

def consultarProducto(request, id): 
    try:
        producto = Producto.objects.get(id=id) 
        categorias = Categoria.objects.all() 
        mensaje=""
    except Error as error: 
        mensaje=f"Problemas al Consultar el Producto {error}"
    retorno = {"mensaje": mensaje, "producto": producto, "listaCategorias": categorias}
    return render(request,"frmEditarProducto.html",retorno)

def actualizarProducto(request):
    
    idProducto = int(request.POST["idProducto"])
    codigo = int(request.POST["txtCodigo"])
    nombre = request.POST["txtNombre"]
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"]) 
    archivo = request.FILES.get("fileFoto", False)
    
    try:
        #obtener la categoria de acuerdo a su id
        categoria = Categoria.objects.get(id=idCategoria)
        #actualizar el producto. PRIMERO SE CONSULTA
        producto = Producto.objects.get(id=idProducto)
        producto.proNombre=nombre
        producto.proPrecio=precio 
        producto.proCategoria=categoria
        producto.proCodigo=codigo
        #si el campo de foto tiene datos actualiza foto
        if(archivo!=''):
            producto.proFoto= archivo
        producto.save()
        mensaje="Producto actualizado correctamente" 
        return redirect("/listarProductos/")
    
    except Error as error:
        mensaje=f"Problemas al realizar el proceso de actualizar el producto {error})"
        
    categorias = Categoria.objects.all()
    retorno = {"mensaje" :mensaje, "listaCategorias":categorias, "producto":producto} 
    return render(request, "frmEditarProducto.html", retorno)

def eliminarProducto(request,id):
    try:
        
        producto = Producto.objects.get(id=id) 
        producto.delete()
        mensaje="Producto Eliminado Correctamente..." 
        
    except Error as error:
        mensaje=f"Problemas al eliminar el producto {error}"
        
    retorno = {"mensaje":mensaje} 
    return redirect("/listarProductos/", retorno)