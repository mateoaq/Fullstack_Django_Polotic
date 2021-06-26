from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    titulo = models.CharField( max_length=64)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categorias")
    descripcion = models.CharField( max_length=300)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="Productos", null=True)

    def __str__(self):
        return f"Producto #{self.id} {self.titulo}, categoria: {self.categoria}, descripción: {self.descripcion}, precio: {self.precio}"





