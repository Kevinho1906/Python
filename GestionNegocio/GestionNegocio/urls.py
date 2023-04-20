from django.contrib import admin
from django.urls import path
from appTienda import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('', views.listarProductos),
    path('vistaCategorias/', views.vistaCategorias),
    path('agregarCategorias/', views.agregarCategorias),
    path('listarProductos/', views.listarProductos),
    path('vistaProductos/', views.vistaProductos),
    path('agregarProducto/', views.agregarProducto),
    path('consultarProducto/<int:id>/', views.consultarProducto),
    path('actualizarProducto/', views.actualizarProducto),
    path('eliminarProducto/<int:id>/', views.eliminarProducto),
]

if settings.DEBUG:
    urlpatterns += static(
        
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT,
        
    )