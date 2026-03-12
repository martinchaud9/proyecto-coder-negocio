from django import forms
from .models import Colchones
from .models import Almohadas
from .models import Clientes

class ColchonForm(forms.ModelForm):
    class Meta: 
        model = Colchones
        fields = ["marca", "modelo", "altura", "densidad", "garantia"]
        widgets = {
            "marca" : forms.TextInput(attrs={'class': 'form-control'}),
            "modelo" : forms.TextInput(attrs={'class': 'form-control'}),
            "altura" : forms.TextInput(attrs={'class': 'form-control'}),
            "densidad" : forms.TextInput(attrs={'class': 'form-control'}),
            "garantia" : forms.TextInput(attrs={'class': 'form-control'}),
            "precio" : forms.NumberInput(attrs ={'class': 'form-control'}), 
        }
        
class AlmohadaForm(forms.ModelForm):
    class Meta:
        model = Almohadas
        fields= ["marca", "modelo"]
        widgets = {
            "marca":forms.TextInput(attrs={'class': 'form-control'}),
            "modelo": forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields=["dni", "nombre", "apellido", "domicilio", "telefono"]
        widgets = {
            "dni": forms.TextInput(attrs={'class' :'form-control' }),
            "nombre": forms.TextInput(attrs= {'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "domicilio" : forms.TextInput(attrs={'class': 'form-control'}),
            "telefono": forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class BuscarClienteForm(forms.Form):
    dni = forms.CharField(label="DNI")

