from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from account.models import Perfil
from account.forms import * 

def register(request):
    if request.method == "POST":
        form = PerfilCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("perfil_detail")
    else:
        # ESTA LÍNEA ES LA QUE FALTA: Crea el formulario vacío para mostrarlo
        form = PerfilCreateForm()
    
    # Aquí pasamos el 'form' al HTML. Si no lo pasas, el HTML no muestra nada.
    return render(request, "account/register.html", {"form": form})
    
@login_required
def profile_detail(request):
    return render(request, "account/perfil_detail.html",{"user": request.user})
#Toda informacion del usuario ya logueado va a estar en request.user


def profile_change(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("perfil_detail")
    else:
        form = PerfilChangeForm(instance = request.user)
    return render(request, "account/perfil_change.html", {"form" : form})