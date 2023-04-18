from django.contrib import admin
from django.urls import path
from appTienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('vistaCategorias/', views.vistaCategorias),
    path('agregarCategorias/', views.agregarCategoria),
    path('listarProductos/', views.listarProductos),
]
