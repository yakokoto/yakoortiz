from django.db import models
import datetime
import datetime
from django.utils import timezone
from django.utils import timezone
from django.utils.timezone import now
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

dia_delta=datetime.timedelta(days=15)
fechainicial=datetime.date.today()
fechafutura=fechainicial+dia_delta


# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    is_recepcionista = models.BooleanField('Is recepcionista', default=False)

class Usuario(models.Model):
    codigo = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo

class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    expediente = models.CharField(max_length=100)
    abogado = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=500)
    fechaen = models.DateField( default=datetime.date.today)
    fechaven = models.DateField( default=fechafutura)
    #diasrestantes = models.IntergerField(default=fechaen-fechaven)
    pdf = models.FileField(upload_to='books/pdfs/')
    #cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

class Provedor(models.Model):
    empresa = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    correo = models.EmailField( max_length=100)
    
class Fiel(models.Model):
    Empresa = models.CharField(max_length=100)
    fiel = models.FileField(upload_to='fiel/')
    ciec = models.FileField(upload_to='ciec/')

class Firma(models.Model):
    Empresa = models.CharField(max_length=100)
    RFC = models.CharField(max_length=100)
    fielkey = models.FileField(upload_to='fielkey/')
    fielcer = models.FileField(upload_to='fielcer/')
    contraseña = models.CharField(max_length=100)


class Contrasena(models.Model):
    Empresa = models.CharField(max_length=100)
    RFC = models.CharField(max_length=100)
    Contrasena = models.FileField(upload_to='Contraseña/')
