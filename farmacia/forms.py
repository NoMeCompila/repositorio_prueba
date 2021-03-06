from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import  Fcia, Provincia, Programa, Localidad, Usuario
from django.contrib.auth.forms import AuthenticationForm

class LocalidadActForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ['estado']
        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })
        labels = {
            'estado' : 'estado de la localidad (Activar/Desactivar)'
        }

# Formulario para agregar localidad //eliminar probablemente 
class LocalidadForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Localidad
        
        fields = ['id_localidad','descripcion','id_provincia_id','estado']

        widgets = {
            'id_localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'id_provincia_id.descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'})

        }

        labels = {
            'id_localidad': 'id de la localidad',
            'id_provincia_id.descripcion': 'provincia a la que pertenece',
            'descripcion': 'nombre de la localidad',
            'estado':'0=activo y 1 = inactivo'
        }

#Formulario para agregar/actualizar un programa
class ProgramaActForm(forms.ModelForm):
    
    class Meta:

        model = Programa
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado del programa (Activar/Desactivar)'
        }



#Formulario para crear farmacia
# class FarmaciaForm(forms.ModelForm):
#     class Meta:     
#         model = Farmacia
#         fields = ['fica_id', 'nombre', 'direccion']

#Formualrio para crear provincia
class ProvinciaForm(forms.ModelForm):
    class Meta:     
        model = Provincia
        fields = ['id_provincia', 'descripcion','estado']
        widgets={
            'id_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'id' : 'id_provincia',
            'descripcion' : 'nombre de la provincia',
            'estado': 'estado'
        }

#Form para actualizar estado de una provincia
class ProvinciaActForm(forms.ModelForm):
    class Meta:     

        model = Provincia
        fields = ['estado']
        widgets={
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'estado': 'estado'
        }

#Formulario para agregar/actualizar un programa
class ProgramaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Programa
        
        fields = ['programa','nombre','version','fecha_install']

        widgets = {
            'programa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_install': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'programa': 'id del programa',
            'nombre': 'nombre del programa',
            'version': 'version del programa actual',
            'fecha_install': 'fecha de instalacion'
        }


# Formulario para activar provincias
class ProvinciaActForm(forms.ModelForm):
    
    class Meta:

        model = Provincia
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la provincia (Activar/Desactivar)'
        }


# Formulario para agregar farmacias
class FciaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Fcia
        
        fields = ['nro_cliente','nombre_facia','id_localidad']

        widgets = {
            'nro_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_facia': forms.TextInput(attrs={'class': 'form-control'}),
            'id_localidad.descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }


        
        labels = {
            
                'nro_cliente': 'n??mero de cliente',
                'nombre_facia': 'nombre de la farmacia',
                'id_localidad.descripcion': 'localidad a la que pertenece'
            }

#Form para actualizar estado de una fcia
class FciaActForm(forms.ModelForm):
    class Meta:

        model = Fcia
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la Fcia (Activo/Inatcivo)'
        }
from django import forms
from django.forms.widgets import Widget
#from django.db import forms
#from django-autocomplete-light import 
from .models import  Fcia, Provincia, Programa, Localidad  #Farmacia,

class LocalidadActForm(forms.ModelForm):
    class Meta:

        model = Localidad
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la localidad (Activar/Desactivar)'
        }

class LocalidadForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Localidad
        
        fields = ['id_localidad','descripcion','id_provincia_id']

        widgets = {
            'id_localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'id_provincia_id.descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})

        }

        # def __init__(self,*args, **kwargs):
        #     super().__init__(*args, **kwargs)

        #     self.fields['id_provincia_id'].widget.attrs.update({
        #         'class': 'form-control'
        #     })

        labels = {
            'id_localidad': 'id de la localidad',
            'id_provincia_id.descripcion': 'provincia a la que pertenece',
            'descripcion': 'nombre de la localidad'
        }

#Formulario para agregar/actualizar un programa
class ProgramaActForm(forms.ModelForm):
    
    class Meta:

        model = Programa
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado del programa (Activar/Desactivar)'
        }



#Formulario para crear farmacia
# class FarmaciaForm(forms.ModelForm):
#     class Meta:     
#         model = Farmacia
#         fields = ['fica_id', 'nombre', 'direccion']

#Formualrio para crear provincia
class ProvinciaForm(forms.ModelForm):
    class Meta:     
        model = Provincia
        fields = ['id_provincia', 'descripcion','estado']
        widgets={
            'id_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'id' : 'id_provincia',
            'descripcion' : 'nombre de la provincia',
            'estado': 'estado'
        }

#Form para actualizar estado de una provincia
class ProvinciaActForm(forms.ModelForm):
    class Meta:     

        model = Provincia
        fields = ['estado']
        widgets={
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'estado': 'estado'
        }

#Formulario para agregar/actualizar un programa
class ProgramaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Programa
        
        fields = ['programa','nombre','version','fecha_install']

        widgets = {
            'programa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_install': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'programa': 'id del programa',
            'nombre': 'nombre del programa',
            'version': 'version del programa actual',
            'fecha_install': 'fecha de instalacion'
        }



class ProvinciaActForm(forms.ModelForm):
    
    class Meta:

        model = Provincia
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la provincia (Activar/Desactivar)'
        }












class FciaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Fcia
        
        fields = ['nro_cliente','nombre_facia','id_localidad']

        widgets = {
            'nro_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_facia': forms.TextInput(attrs={'class': 'form-control'}),
            'id_localidad.descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'nro_cliente': 'n??mero de cliente',
            'nombre_facia': 'nombre de la farmacia',
            'id_localidad.descripcion': 'localidad a la que pertenece'
        }




#Formulario para los usuarios
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'form-control'
        self.fields['usuario'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contrase??a'

#Formulario de registro de usuarios en la base de datos

class FormularioUsuarios(forms.ModelForm):
    
    password1 = forms.CharField(label='Contrase??a', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contrase??a',
            'id': 'password1',
            'required':'required'
        }
    ))

    password2 = forms.CharField(label='Confirmar Contrase??a', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contrase??a ',
            'id': 'password2',
            'required':'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('usuario','nombre','apellido')
        widgets = {

            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                }
            ),

            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido',
                }
            ),

            'usuario':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su usuario',
                }
            ),
        }
         