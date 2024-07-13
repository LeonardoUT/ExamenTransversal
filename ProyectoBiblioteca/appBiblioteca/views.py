from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    Jumbo = Jumbotron.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav,
        "Jumbotron": Jumbo
    }
    return render(request, 'core/index.html', context)

def autores(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    Autor = Autores.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav,
        "Autor" : Autor
    }
    return render(request, 'core/autores.html', context)

def libros(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    Libro = Libros.objects.all()
   
    form = BuscarLibro()
    
    if request.method == 'POST':
        form = BuscarLibro(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            Libro = Libros.objects.filter(titulo__icontains=title)
            if not Libro.exists():
                mensaje = "No se ha encontrado el libro."
        
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav,
        "Libro" : Libro
    }
    return render(request, 'core/libros.html', context)

def catalogo(request):
    Navbars = Navbar.objects.all()
    Titulonav = TituloNav.objects.all()
    Catalogos = Categoria.objects.all()
    context = {
        "Navbars": Navbars,
        "Titulonav": Titulonav,
        "Catalogos" : Catalogos
    }
    return render(request, 'core/catalogo.html', context)

