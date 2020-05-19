"""mysiteDiamanti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include,path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
] # La funzione path() passa quattro argomenti, due richiesti: ruote e view, e due opzionali: kwargs e name. A questo punto
# route: stringa che contiene l'url
# view: quando si trova un url viene richiamata la view.py dove fara' presente della funzione view associata
#kwargs: -
#name: dare un nome all'url lascia la possibilita' di riferire da altre parti di Django (usato molto nei template)

#Creazione di un progetto Django
#Il primo comando da utilizzare per creare un progetto e':"django-admin startproject mysiteCognome"
#con questo comando viene creata una directory con il nome indicato dove e' possibile lavorare sul progetto
#dopodiche' si entra nella directory e si manda il comando "python manage.py startapp polls" in modo che verra' creata
#una app col nome indicato ("polls") dove viene immagazzinata la parte inerente ai sondaggi (polls)

# I comandi migrate e makemigrations prendono tutte le migrazioni che non sono state applicate e le esegue contro il tuo database,
# sincronizzando i cambiamenti che hai fatto nel tuo model
#I tre passi principali sono:
#1. modificare il modello (models.py)
#2. eseguire python manage.py makemigrations (per creare le migrazioni con i cambiamenti)
#3. eseguire python manage.py migrate per applicare i cambiamenti nel database

#Hardcoded URLs
#Il problema con questi url e' la difficolta' nel cambiarli in caso di modifiche in progetti con molti template. Tuttavia, siccome abbiamo
#definito l'argomento "name" nella funzione path() nel modulo polls.urls. Si puo' vedere dove il nome URL di detail viene definito (name='detail')

#Namespacing URL
#Django utilizza una sintassi precisa di python che permette di richiamare semplicemente (soprattutto per un utente esperto) gli url dalle altre pagine .py.
#Gli urls vengono salvati nella pagina urls.py di polls, e vengono richiamati tra parentesi graffe nelle pagine html
#es.: {% url 'polls:detail' question.id %}

#request.POST
#request.POST[''] e' un oggetto che permette di accedere ai dati del nome chiave. In questo caso, request.POST['choice'] ritorna l'ID della scelta selezionata come stringa request.POST (i valori sono sempre stringhe).

#reverse()
#La funzione reverse() nel costruttore HttpResponseRedirect aiuta ad evitare l'utilizzo di Hardcoded URLs nella view. Gli viene dato il nome della view che vogliamo passargli controllo e la porzione di utl che indirizza alla view.
#Nel caso nostro, al reverse() richiama una stringa tipo: '/polls/3/results/'
#dove il 3 e' il valore dell'id di question (question.id). L'URL rindirizzato richiama la view di results da mostrare nella pagina finale.