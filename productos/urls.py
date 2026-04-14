from django.urls import path
from productos.views import *


urlpatterns = [
    #URLS COLCHONES
    path("", inicio, name="inicio"),#"" para indicar ruta vacia,inicio(funcion de vista que se ejecuta), #name es el nombre para referenciar la url
    path("agregar_colchon/", agregar_colchon, name= "agregar_colchon"),
    path("colchones/", mostrar_colchones, name = "mostrar_colchones"),
    path('colchon/editar/<int:pk>/', ColchonUpdateView.as_view(), name= "colchon_update"),
    path('colchon/eliminar/<int:pk>/', ColchonDeleteView.as_view(), name = "colchon_delete"),
    
    
    #URLS ALMOHADAS
    path("agregar_almohada/", agregar_almohada, name="agregar_almohada" ),
    path("almohadas/", mostrar_almohadas, name = "mostrar_almohadas"),
    path("almohada/editar/<int:pk>/", AlmohadaUpdateView.as_view(), name="almohada_update"),
    path("almohada/eliminar/<int:pk>/", AlmohadaDeleteView.as_view(), name ="almohada_delete"),
    
    #URLS CLIENTES
    path("clientes/", mostrar_clientes, name = "mostrar_clientes"),
    path("agregar_cliente/", agregar_cliente, name = "agregar_cliente"),
    path("buscar_cliente/", buscar_cliente, name="buscar_cliente"),
    path("cliente/editar/<int:pk>/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("cliente/eliminar/<int:pk>/", ClienteDeleteView.as_view(), name="cliente_delete"),
    
    #A cerca de mi
    path('about/', about, name='about'),
    
]