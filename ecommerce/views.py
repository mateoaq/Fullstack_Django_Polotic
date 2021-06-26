from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import Producto
from django.contrib.auth.models import User
from .carrito import Carrito

# Create your views here.
def index(request):
    
    principales = Producto.objects.all()[:3]
    productos = Producto.objects.all()[3:10]

    return render(request, "index.html", {
        "principales": principales,
        "productos": productos
    })


def about(request):
    return render(request, "about.html")


def product(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto.html', {
        'producto': producto
    })


@login_required
@permission_required('can_add_producto')
def nuevo_producto(request):

    if request.method == 'POST':
        form = Nuevoproducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = Nuevoproducto()
        return render(request, 'nuevo_producto.html', {
            'form':form
        })

@login_required
@permission_required('can_delete_producto')
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
@permission_required('can_edit_producto')
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = Nuevoproducto(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = Nuevoproducto(instance = producto)
        return render(request, 'editar_producto.html', {
                'producto': producto,
                'form':form
            })


def login(request):
    form = LoginForm()
    return render(request, "registration/login.html", {
        'form':form
    })


def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()        
            username = form.cleaned_data['username']
            messages.success(request, f'¡Usuario {username} creado satisfactoriamente!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })
    return render(request, "registration/registro.html")

@login_required
def carrito(request):
    carrito = Carrito(request)
    total = carrito.total()
    user_id = request.user.id
    return render(request, "carrito.html", {
         "carrito": carrito,
         "total": total,
         "user": request.user,
         "user_id": user_id,
     })

@login_required
def carrito_add(request, producto_id):
     carrito = Carrito(request)
     producto = Producto.objects.get(id=producto_id)
     carrito.add(producto)
     return HttpResponseRedirect(reverse('carrito'))

@login_required
def carrito_decre(request, producto_id):
     carrito = Carrito(request)
     producto = Producto.objects.get(id=producto_id)
     carrito.decrementar(producto)
     return HttpResponseRedirect(reverse('carrito'))

@login_required
def carrito_del(request, producto_id):
     carrito = Carrito(request)
     producto = Producto.objects.get(id=producto_id)
     carrito.remove(producto)
     return HttpResponseRedirect(reverse('carrito'))

@login_required
def carrito_clear(request):
     carrito = Carrito(request)
     carrito.clear()
     return HttpResponseRedirect(reverse('carrito'))

def search(request, cat_id = ""):
    search = request.GET.get("search")
    if cat_id != "":
        productos = Producto.objects.all().filter(categoria=cat_id)
        return render(request, "search.html", {
        "productos": productos
    })

    if search:
        productos = Producto.objects.all().filter(titulo__startswith=search)
        return render(request, "search.html", {
        "productos": productos
    })






