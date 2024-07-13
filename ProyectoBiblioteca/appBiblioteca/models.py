from django.db import models

# Create your models here.

class TituloNav(models.Model):
    titulo = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo

class Navbar(models.Model):
    id_navbar = models.AutoField(db_column= "idNavbar", primary_key= True )
    enlac = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.enlac
    def __str__(self):
        return self.url

class Autores(models.Model):
    nombre = models.CharField(max_length= 150)
    nacionalidad = models.CharField(max_length= 50)
    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.nacionalidad

class Libros(models.Model):
    titulo = models.CharField(max_length=150)
    annioPublicacion = models.IntegerField()
    descripcion = models.TextField()
    
class Categoria(models.Model):
    nombre = models.CharField(max_length= 150)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
    def __str__(self):
        return self.descripcion
    
class Jumbotron(models.Model):
    titulo = models.CharField(max_length= 100)
    contenido = models.CharField(max_length= 255)
    def __str__(self):
        return self.titulo
    def __str__(self):
        return self.contenido
    

        
    
    
    