from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from invia.models import Ticket
from .forms import Registration, Login, RecuperaPasswordForm
from .models import Persona
from django.contrib.auth.models import User
# Create your views here.

@login_required
def Ricevuti(request):
    pk = request.user.id
    user = User.objects.get(pk=pk)
    dati = Ticket.objects.filter(reparto_destinatario=user.first_name).order_by('-data_richiesta')
    return render(request, 'ricevi.html', {'dati':dati})

def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            reparto = form.cleaned_data['reparto']
            password = form.cleaned_data['password']
            
            user = User.objects.create(
                username = username,
                email=email,
                password = password,
                first_name = reparto
            )
            #user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('bacheca')
    else:
        form = Registration()
    context = {'form':form}
    return render(request, 'registration/create_account.html', context)

def logins(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = User.objects.get(username=username, password=password)
            print(user)
            login(request, user)
            return redirect('bacheca')
    else:
        form = Login()
    
    context = {'form':form}
    return render(request, 'registration/login.html', context)

def logouts(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def recuperaPassword(request):
    stringa = ""
    if request.method == 'POST':
        form = RecuperaPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            conferma_password = form.cleaned_data['conferma_password']
            if password == conferma_password:
                try:
                    user = User.objects.get(username=username)
                    stringa = "password cambiata con successo"
                    user.password = password
                    user.save()
                except Exception:
                    stringa = "lo username non cambacia con nessuno nel database. Riprova!"
                    return render(request, 'registration/password_persa.html', {"form":form, "stringa":stringa})
            else:
                stringa = "errore nel cambiare la password"
    else:
        form = RecuperaPasswordForm()
    context = {"form":form, "stringa":stringa}
    return render(request, 'registration/password_persa.html', context)
        