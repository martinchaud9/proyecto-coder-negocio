from django.db import models

class Colchones(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    altura = models.CharField(max_length=50)
    densidad = models.CharField(max_length=50)
    garantia = models.CharField(max_length=50)

    
    
def __str__(self):
    return f"Colchon {self.marca} de {self.modelo} con una altura de {self.altura} y un soporte de hasta {self.densidad}, con una garantia de {self.garantia} años."


class Almohadas(models.Model):
    marca= models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
def __str__(self):
    return f"Almohada {self.marca} {self.modelo}"

class Clientes(models.Model):
    dni= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    

def __str__(self):
    return f"{self.nombre} {self.apellido} {self.dni}"

    