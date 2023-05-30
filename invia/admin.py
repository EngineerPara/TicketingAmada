from django.contrib import admin
from .models import Ticket

# Register your models here.
class AdminTicket(admin.ModelAdmin):
    model=Ticket
    list_filter=['reparto_richiedente','data_richiesta', 'priorità']
    list_display = ('richiedente', 'reparto_destinatario', 'reparto_richiedente',
                    'data_richiesta','priorità', 'data_evasione_richiesta', 'data_evasione_effettiva',
                    'descrizione',)
    search_fields= ['reparto_richiedente', 'data_richiesta', 'priorità']

admin.site.register(Ticket, AdminTicket)