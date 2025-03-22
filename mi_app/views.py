from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.http import JsonResponse

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_app/productos.html', {'productos': productos})

#views.py
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ProductoForm()  # Se crea un formulario vacío para la vista GET
    
    return render(request, 'mi_app/crear_producto.html', {'form': form})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ProductoForm(instance=producto)  # Muestra el formulario con datos del producto
    
    return render(request, 'mi_app/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')  # Redirige directamente después de eliminar