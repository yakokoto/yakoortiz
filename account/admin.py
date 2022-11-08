from django.contrib import admin
from account.models import Usuario
from account.models import Documento
from account.models import User, Provedor, Firma, Contrasena



# Register your models here.
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display=('titulo','abogado','comentarios','fechaen','fechaven','pdf')
    ordering=('titulo',)
    search_fields=('titulo','abogado','comentarios','fechaen','fechaven','pdf')
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('codigo','comentario')
    ordering=('codigo',)
    search_fields=('codigo','comentario')
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','is_admin','is_customer','is_employee','is_recepcionista')
    ordering=('username',)
    search_fields=('username','email','is_admin','is_customer','is_employee','is_recepcionista')

@admin.register(Provedor)
class ProvedorAdmin(admin.ModelAdmin):
    list_display=('empresa','nombre','celular','correo')
    ordering=('empresa',)
    search_fields=('empresa','nombre','celular','correo')

@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    list_display=('Empresa','RFC','fielkey','fielcer', 'contraseña')
    ordering=('Empresa',)
    search_fields=('Empresa','RFC','fielkey','fielcer', 'contraseña')

@admin.register(Contrasena)
class ContrasenaAdmin(admin.ModelAdmin):
    list_display=('Empresa','RFC', 'Contrasena')
    ordering=('Empresa',)
    search_fields=('Empresa','RFC', 'Contrasena')