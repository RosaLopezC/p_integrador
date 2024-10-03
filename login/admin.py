from django.contrib import admin
from .models import Usuario  # Importa tu modelo Usuario

# Clase de administración personalizada para mostrar los campos en formato tabla
class UsuarioAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en forma de columnas
    list_display = ('nombre', 'fecha_nacimiento', 'correo', 'tipo_cuenta')

    # Añade la opción de buscar por nombre o correo
    search_fields = ('nombre', 'correo')

    # Añade filtros por tipo de cuenta
    list_filter = ('tipo_cuenta',)

# Registra el modelo Usuario con la configuración personalizada
admin.site.register(Usuario, UsuarioAdmin)
