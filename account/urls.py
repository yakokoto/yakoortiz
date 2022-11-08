from django import views
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.urls import include, path
from django.urls import include, path
from . import views
from . import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('', views.login_view, name='login_view'),
    path('alta_nuevo/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('recepcionista/', views.recepcionista, name='recepcionista'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('base/', views.base, name='base'),
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/upload/', views.upload_usuario, name='upload_usuario'),
    path('logout/', views.logout_request, name="logout"),
    path('admin/', views.admin, name="admin"),
    path('upload', views.upload, name="upload"),
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/upload/', views.upload_proveedor, name='upload_proveedor'),
    path('firmas/', views.firma_list, name='firma_list'),
    path('firmas/upload/', views.upload_firma, name='upload_firma'),
    path('contrasenas/', views.contrasena_list, name='contrasena_list'),
    path('contrasenas/upload/', views.upload_contrasena, name='upload_contrasena'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)