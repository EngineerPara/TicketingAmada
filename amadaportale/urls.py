"""
URL configuration for amadaportale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bacheca.views import home, ScriviBacheca, bacheca, bacheca_details
from invia.views import InviaPage, Cerca, Details, ModificaTicket, EliminaTicket
from ricevi.views import Ricevuti, logins, registration, logouts, recuperaPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bacheca, name='bacheca'),
    path('invia/', InviaPage, name='invia'),
    path('cerca/', Cerca, name='cerca'),
    path('dettagli/<int:pk>', Details, name='details'),
    path('ricevi/', Ricevuti, name='ricevi'),
    path('registration/', registration,name='registration'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
    path('crea_post/', ScriviBacheca, name='post_creazione'),
    path('bacheca_details/<int:pk>', bacheca_details, name='details_post'),
    #path('bacheca/', bacheca, name='bacheca'),
    path('modifica_ticket/<int:pk>', ModificaTicket, name='modifica_ticket'),
    path('elimina_ticket/<int:pk>', EliminaTicket, name='elimina_ticket'),
    path('recupera_password/', recuperaPassword, name='recupera_password'),
]
