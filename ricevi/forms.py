from django import forms
from .models import Persona
from django.contrib.auth.models import User

# class Registration(forms.Form):
#     # name = forms.CharField()
#     # email = forms.EmailField()
#     username = forms.CharField()
#     
#     email = forms.EmailField()
#     reparto = forms.ChoiceField(
#         choices=(('Logistica','Logistica'), ('Accounting','Accounting'), ('General Admin','General Admin'),('Service','Service'), 
#                ('Sales','Sales'), ('IT', 'IT'), ('Marketing', 'Marketing'),('Direzione','Direzione'),)
#     )

# class Login(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())


class Registration(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.CharField(widget=forms.EmailField())
    reparto = forms.ChoiceField(
    choices=(('Logistica','Logistica'), ('Accounting','Accounting'), ('General Admin','General Admin'),('Service','Service'), 
               ('Sales','Sales'), ('IT', 'IT'), ('Marketing', 'Marketing'),('Direzione','Direzione'),))
    
    class Meta:
        model = User
        fields = ["username", "email"]
        
class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget = forms.PasswordInput())
    

class RecuperaPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    conferma_password = forms.CharField(widget=forms.PasswordInput())