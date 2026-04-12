from django.db import models
from django.contrib.auth.models import AbstractUser
import random
#AbstractUser es el modelo de la tabla user de la bd de django
#Entonces nuestro nuevo modelo va a tener los atributos de los user de la bd de django mas lo que le agreguemos en perfil

#MI CARPETA PROYECTO-CODER ES DE CONFIGURACION

#La instancia va a ser el objeto perfil que se va a querer guardar y el nombre del archivo
def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"#Esto crea una carpeta para cada usuario dentro de la carpeta media con todas las imagenes de cada uno de los usuarios

def get_user_number():
    number = random.randint(0, 1000000)
    for i in range (10):
        perfil = Perfil.objects.filter(nro_usuario = number)
        if perfil.exists():
            number = random.randint(0, 1000000)
        else: 
            return number
        
class Perfil(AbstractUser):
    avatar = models.ImageField(
        #Esta f renombra la imagen y lo va a guatrdar en una carpeta 
        upload_to= avatar_upload_to,
        #La imagen default cuando se crea un avatar
        default = "default/default.png",
        blank=True,
        verbose_name = "Avatar" #Esto es un apaodo
    )
    pais = models.CharField(max_length=50)
    dni = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    nro_usuario= models.IntegerField(unique=True, default=get_user_number)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    
    def _str__(self):
        return  f"Perfil: {self.email} - {self.first_name}, {self.last_name} / Nro: {self.nro_usuario}"