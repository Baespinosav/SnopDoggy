from django.contrib import admin
from .models import Categoria, manProducto, Vehiculo, categoriaProducto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(categoriaProducto)
admin.site.register(manProducto)
