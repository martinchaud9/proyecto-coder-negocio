from django.contrib import admin
from .models import Colchones
from .models import Almohadas
from .models import Clientes

@admin.register(Colchones)
class ColchonesAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("marca", "modelo", "altura", "densidad", "garantia")
    # Columnas con enlaces clickeables para entrar al detalle
    list_display_links = ("marca", )
    # Campos por los que buscar los registros
    search_fields = ("marca", "modelo", "densidad")
    
    
@admin.register(Almohadas)
class AlmohadasAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("marca", "modelo")
    # Columnas con enlaces clickeables para entrar al detalle
    list_display_links = ("marca", )
    # Campos por los que buscar los registros
    search_fields = ("marca", "modelo")
    
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("dni", "nombre", "apellido", "domicilio", "telefono")
    # Columnas con enlaces clickeables para entrar al detalle
    list_display_links = ("dni", )
    # Campos por los que buscar los registros
    search_fields = ("nombre",)
    
    

