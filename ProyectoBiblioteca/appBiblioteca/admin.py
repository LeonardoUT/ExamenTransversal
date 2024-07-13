from django.contrib import admin
from .models import Navbar, TituloNav, Autores, Libros, Categoria, Jumbotron

# Register your models here.
admin.site.register(Navbar)
admin.site.register(TituloNav)
admin.site.register(Autores)
admin.site.register(Libros)
admin.site.register(Categoria)
admin.site.register(Jumbotron)