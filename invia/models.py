from django.db import models
from datetime import datetime

# Create your models here.

class Ticket(models.Model):
    titolo = models.CharField(max_length=20, default="")
    richiedente = models.CharField(max_length=50)
    reparto_destinatario = models.CharField(max_length=50, default="Logistica", editable=False)
    reparto_richiedente = models.CharField(max_length=50)
    data_richiesta = models.DateField(default=str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day))
    priorità = models.CharField(max_length=15)
    data_evasione_richiesta = models.DateField()
    data_evasione_effettiva = models.DateField(default=str(datetime.now().year)+"-"+str(datetime.now().month)+"-"+str(datetime.now().day))
    descrizione = models.TextField()
    progress = models.CharField(default="Non Accettato", max_length=20)
    note = models.TextField(default="")

    # def __init__(self, richiedente, reparto_destinatario, reparto_richiedente,data_richiesta, priorità,data_evasione_richiesta,
    #              descrizione):
    #     self.richiedente = richiedente
    #     self.reparto_destinatario = reparto_destinatario
    #     self.reparto_richiedente = reparto_richiedente,
    #     self.data_richiesta = data_richiesta
    #     self.priorità = priorità,
    #     self.data_evasione_richiesta = data_evasione_richiesta
        

    class Meta:
        verbose_name_plural = 'Tickets'
        