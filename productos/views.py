from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from productos.forms import ColchonForm
from productos.forms import AlmohadaForm
from productos.forms import ClienteForm
from productos.forms import BuscarClienteForm
from productos.models import Colchones
from productos.models import Almohadas
from productos.models import Clientes
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "productos/inicio.html")

@login_required
def agregar_colchon(request):
    if request.method == 'POST': 
        form = ColchonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar_colchones")
    else: 
        form = ColchonForm()
    return render(request, "productos/agregar_colchon.html",{"form": form})

@login_required
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


class ColchonUpdateView(LoginRequiredMixin,UpdateView):
    model = Colchones
    fields=["marca", "modelo", "altura", "densidad", "garantia"]
    template_name = 'productos/agregar_colchon.html'
    success_url = reverse_lazy('mostrar_colchones')
    
class ColchonDeleteView(LoginRequiredMixin, DeleteView):
    model = Colchones
    template_name = 'productos/colchon_confirm_delete.html'
    success_url = reverse_lazy('mostrar_colchones')
    
#ALMOHADAS:
@login_required
def agregar_almohada(request):
    if request.method == 'POST':
        form = AlmohadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar_almohadas")
    else:
        form = AlmohadaForm()
    return render(request, "productos/agregar_almohada.html", {'form': form})

class AlmohadaUpdateView(LoginRequiredMixin, UpdateView):
    model= Almohadas
    fields= ["marca", "modelo"]
    template_name = 'productos/agregar_almohada.html'
    success_url = reverse_lazy('mostrar_almohadas')
    
class AlmohadaDeleteView(LoginRequiredMixin, DeleteView):
    model = Almohadas
    template_name = 'productos/almohada_confirm_delete.html'
    success_url = reverse_lazy('mostrar_almohadas')

@login_required
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





#CLIENTES
@login_required
def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar_clientes")
    else:
        form = ClienteForm()    
    return render(request, "productos/agregar_cliente.html", {'form': form})
    
@login_required
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

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields=["dni", "nombre", "apellido", "domicilio", "telefono"]
    template_name = "productos/agregar_cliente.html"
    success_url = reverse_lazy("mostrar_clientes")
    
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = "productos/cliente_confirm_delete.html"
    success_url = reverse_lazy("mostrar_clientes")
        
@login_required
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

#A cerca de mi 
@login_required
def about(request):
    return render(request, "productos/about.html")