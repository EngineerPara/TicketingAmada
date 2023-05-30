from django.contrib import admin
from .models import Persona
# Register your models here.

class AdminPersona(admin.ModelAdmin):
    model=Persona
    list_filter=['email','reparto']
    list_display = ('email', 'reparto',)
    search_fields= ['email', 'reparto']

#admin.site.register(Persona, AdminPersona)