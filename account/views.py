from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import FileSystemStorage
from .forms import UsuarioForm, DocumentoForm, SignUpForm, LoginForm, ProvedorForm, ProvedorForm, FielForm,FielForm,FirmaForm, FirmaForm, ContrasenaForm, ContrasenaForm
from .models import Provedor, Usuario, Documento, Fiel,Fiel, Firma, Contrasena, Contrasena
from django.db.models import Q
from django.conf import settings
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.core.mail import EmailMessage, send_mail
from django.contrib import  messages
from django.contrib import  messages
from django.contrib.auth import  logout



def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            elif user is not None and user.is_recepcionista:
                login(request, user)
                return redirect('recepcionista')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def recepcionista(request):
    return render(request,'recepcionista.html')

def base(request):
    return render(request,'base.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['documento']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def book_list(request):
    busqueda = request.POST.get("buscar")
    documentos = Documento.objects.all()

    if busqueda:
        documentos = Documento.objects.filter(
            Q(titulo__icontains = busqueda) | 
            Q(abogado__icontains = busqueda) |
            Q(comentarios__icontains = busqueda) |
            Q(fechaen__icontains = busqueda) |
            Q(fechaven__icontains = busqueda)
        ).distinct()
    return render(request, 'book_list.html', {
        'documentos': documentos})


def firma_list(request):
    busqueda = request.POST.get("buscar")
    firmas = Firma.objects.all()

    if busqueda:
        firmas = Firma.objects.filter(
            Q(Empresa__icontains = busqueda) |
            Q(RFC__icontains = busqueda)
        ).distinct()
    return render(request, 'firma_list.html', {
        'firmas': firmas})







def proveedor_list(request):
    busqueda = request.POST.get("buscar")
    proveedores = Provedor.objects.all()

    if busqueda:
        proveedores = Provedor.objects.filter(
            Q(nombre__icontains = busqueda) | 
            Q(empresa__icontains = busqueda) |
            Q(celular__icontains = busqueda) |
            Q(correo__icontains = busqueda) 
            ).distinct()
    return render(request, 'proveedor_list.html', {
        'proveedores': proveedores})



def upload_book(request):
    if request.method == 'POST':
        #subject=request.POST["asunto"]
        message="El nombre del documento es" + " " + request.POST["titulo"] + "\n" + "El abogado que subio este documento fue" + " " +request.POST["abogado"] + "\n" + "los comentarios del documento fueron:" + " " + request.POST["comentarios"] + "\n" + "la fecha en la que se subió el documento fue" + " " + request.POST["fechaen"] + "\n" + "la fecha en la que se vence el documento es" + " " + request.POST["fechaven"] + "\n" 
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['yakoortiz@gmail.com','lafconsultoriasistemas@gmail.com']
        email=EmailMessage('Laf consultores', message , email_from, recipient_list)
        #email.attach_file=request.FILES['pdf']
        file=request.FILES['pdf']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = DocumentoForm()
    return render(request, 'upload_book.html', { 
        'form': form 
        })

def usuario_list(request):
    busqueda = request.POST.get("buscar")
    usuarios = Usuario.objects.all()

    if busqueda:
        usuarios = Usuario.objects.filter(
            Q(codigo__icontains = busqueda) | 
            Q(comentario__icontains = busqueda)
        ).distinct()
    
    return render(request, 'usuario_list.html', {
        'usuarios': usuarios})



def upload_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'upload_usuario.html', { 
        'form': form 
        })




def upload_proveedor(request):
    if request.method == 'POST':
        form = ProvedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProvedorForm()
    return render(request, 'upload_proveedor.html', { 
        'form': form 
        })


def upload_firma(request):
    if request.method == 'POST':
        form = FirmaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('firma_list')
    else:
        form = FirmaForm()
    return render(request, 'upload_firma.html', { 
        'form': form 
        })



def logout_request(request):
    logout(request)
    #messages.success(request, "Has cerrado tu sesión")
    #messages.info(request, "vuelve a iniciar sesión")
    return redirect("login_view")
    #return render(request,'index.html')

def contrasena_list(request):
    busqueda = request.POST.get("buscar")
    contrasenas = Contrasena.objects.all()

    if busqueda:
        contrasenas = Contrasena.objects.filter(
            Q(Empresa__icontains = busqueda) |
            Q(Contrasena__icontains = busqueda) |
            Q(RFC__icontains = busqueda)
            ).distinct()
    return render(request, 'contrasena_list.html', {
        'contrasenas': contrasenas})

def upload_contrasena(request):
    if request.method == 'POST':
        form = ContrasenaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contrasena_list')
    else:
        form = ContrasenaForm()
    return render(request, 'upload_contrasena.html', { 
        'form': form 
        })