from django.db import models
from django.conf import settings # Importa esto
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='blog/', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    # CAMBIA ESTA LÍNEA: 
    # Usamos settings.AUTH_USER_MODEL en lugar de User directamente
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} | {self.autor}"