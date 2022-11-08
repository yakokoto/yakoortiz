from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Provedor, User, Firma
from .models import Usuario, Documento, User, Provedor, Fiel, Firma, Contrasena


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('codigo',  'comentario',)

class ProvedorForm(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = ('empresa', 'nombre', 'celular', 'correo')
    
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('titulo', 'expediente','abogado',  'comentarios', 'fechaen', 'fechaven', 'pdf',)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer', 'is_recepcionista')

    class FielForm(forms.ModelForm):
        class Meta:
            model = Fiel
            fields = ('Empresa', 'fiel', 'ciec')

class FielForm(forms.ModelForm):
    class Meta:
        model = Fiel
        fields = ('Empresa', 'fiel', 'ciec')

class FirmaForm(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ('Empresa', 'RFC', 'fielkey', 'fielcer', 'contraseña')

class ContrasenaForm(forms.ModelForm):
    class Meta:
        model = Contrasena
        fields = ('Empresa', 'RFC', 'Contrasena')