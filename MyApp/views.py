from django.shortcuts import render
from .forms import LibroForm
from django.http import HttpResponseRedirect
from .models import Libro

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')  # Ruta a la que se redirige después de la creación del libro
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})

