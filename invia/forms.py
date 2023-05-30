from django import forms

class Invia(forms.Form):
    CHOICES = (('Logistica','Logistica'), ('Accounting','Accounting'), ('General Admin','General Admin'),('Service','Service'), 
               ('Sales','Sales'), ('IT', 'IT'), ('Marketing', 'Marketing'),('Direzione','Direzione'),)
    #richiedente = forms.CharField()
    #reparto_destinatario = forms.CharField()
    #reparto_richiedente = forms.ChoiceField(choices=CHOICES)
#     data_richiesta = forms.DateField(
#     widget=forms.TextInput(     
#         attrs={'type': 'date'} 
#     )
# )      
    titolo = forms.CharField()
    priorità = forms.ChoiceField(
        choices=(('Basso','Basso'), ('Medio','Medio'), ('Urgenza','Urgenza'),)
    )
    data_evasione_richiesta = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
)      
    # data_evasione_effettiva = forms.DateField(
    # widget=forms.TextInput(     
    #     attrs={'type': 'date'} 
    # )
#)      
    #tempo_impiegato = forms.DurationField()
    descrizione = forms.CharField(widget=forms.Textarea())
    
class ResponseTicket(forms.Form):
    data_evasione_effettiva = forms.DateField(
        
        required=False,
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
    
) 
    progress = forms.ChoiceField(choices=(("In Corso", "In corso"), ("Chiuso", "Chiuso")), 
        required=False
                                 )
    note = forms.CharField(widget=forms.Textarea(), required=False)
       
