from django.shortcuts import render, redirect
from productos.forms import ColchonForm
from productos.forms import AlmohadaForm
from productos.forms import ClienteForm
from productos.forms import BuscarClienteForm
from productos.models import Colchones
from productos.models import Almohadas
from productos.models import Clientes

def inicio(request):
    return render(request, "productos/inicio.html")

def agregar_colchon(request):
    if request.method == 'POST': 
        form = ColchonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else: 
        form = ColchonForm()
    return render(request, "productos/agregar_colchon.html",{"form": form})

def mostrar_colchones(request):
    marca = request.GET.get("marca")
    colchones_query = Colchones.objects.all()
    if marca is not None:
        colchones_query = Colchones.objects.filter(
            marca__icontains = marca
        )
    context={
            "lista_colchones": colchones_query
    }
    return render(request, 'productos/mostrar_colchones.html', context)

def agregar_almohada(request):
    if request.method == 'POST':
        form = AlmohadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AlmohadaForm()
    return render(request, "productos/agregar_almohada.html", {'form': form})


def mostrar_almohadas(request):
    marca = request.GET.get("marca")
    almohadas_query = Almohadas.objects.all()
    if marca is not None:
        almohadas_query= Almohadas.objects.filter(
            marca__icontains = marca
        )
    context = {
        "lista_almohadas": almohadas_query
    }
    return render(request, "productos/mostrar_almohadas.html", context)


def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ClienteForm()    
    return render(request, "productos/agregar_cliente.html", {'form': form})
    
    
def mostrar_clientes(request):
    dni= request.GET.get("dni")
    clientes_query = Clientes.objects.all()
    if dni is not None:
        clientes_query = Clientes.objects.filter(
            dni__icontains = dni
        )
    context={
        "lista_clientes" : clientes_query
    }
    return render(request, "productos/mostrar_clientes.html", context)
        
def buscar_cliente(request):

    if request.method == "GET":

        form = BuscarClienteForm(request.GET)

        if form.is_valid():

            dni = form.cleaned_data["dni"]

            resultados = Clientes.objects.filter(dni=dni)

            return render(
                request,
                "productos/resultados_busqueda.html",
                {"resultados": resultados, "form": form},
            )

    else:
        form = BuscarClienteForm()

    return render(request, "productos/buscar_cliente.html", {"form": form})