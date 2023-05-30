from django.shortcuts import render, get_object_or_404, redirect
from .forms import Invia, ResponseTicket
from .models import Ticket
from django.contrib.auth.models import User


# Create your views here.

def InviaPage(request):
    if request.user.pk is not None:
        pk = request.user.pk
        print(pk)
        user = User.objects.get(pk=pk)
        print('sono dentro') 
        if request.method == 'POST':
            print('sono dentro')
            form = Invia(request.POST)
            if form.is_valid():
                titolo = form.cleaned_data['titolo']
                descrizione = form.cleaned_data['descrizione']
                priorità = form.cleaned_data['priorità']
                data_evasione_richiesta = form.cleaned_data['data_evasione_richiesta']
                #data_evasione_effettiva = form.cleaned_data['data_evasione_effettiva']
                #tempo_impiegato = form.cleaned_data['tempo_impiegato']
                #reparto_destinatario = form.cleaned_data['reparto_destinatario']
                Ticket.objects.create(richiedente=user.username,
                                    reparto_richiedente=user.first_name,
                                    titolo = titolo,
                                    descrizione=descrizione,
                                    priorità=priorità,
                                    data_evasione_richiesta=data_evasione_richiesta,
                                    )

        else:
            form = Invia()
        context = {'form':form}
        return render(request, 'invia.html', context)
    return render(request, 'invia.html')


def Cerca(request):
    if 'q' in request.GET:
        queryset = request.GET.get('q')
        queryset = queryset.capitalize()
        reparto_richiedente = Ticket.objects.filter(reparto_richiedente__icontains=queryset)
        #priorità = Ticket.objects.filter(priorità__icontaint=queryset)
        context = {'reparto_richiedente':reparto_richiedente}
        return render(request, 'cerca.html', context)
    else:
        return render(request, 'cerca.html')
    

def Details(request, pk):
    obj = get_object_or_404(Ticket, pk=pk)
    context = {'obj':obj}
    return render(request, 'details.html', context)

def ModificaTicket(request, pk):
    obj = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = ResponseTicket(request.POST)
        if form.is_valid():
            data_evasione_effettiva = form.cleaned_data['data_evasione_effettiva']
            progress = form.cleaned_data['progress']
            note = form.cleaned_data['note']
            if data_evasione_effettiva is not None:
                obj.data_evasione_effettiva = data_evasione_effettiva
            if progress is not None:
                obj.progress = progress
            if note is not None:
                obj.note += "\n"+note
            obj.save()
            redirect(f'/dettagli/{pk}')
    else:
        form = ResponseTicket()
    context = {'form':form, 'obj':obj}
    return render(request, 'modificaticket.html', context)

def EliminaTicket(request, pk):
    obj = get_object_or_404(Ticket, pk=pk)
    obj.delete()
    return render(request, 'elimina_ticket.html')