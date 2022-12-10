from django.shortcuts import render
from AppCoder.models import padre, madre, hermano

# Create your views here.
def familiares(request):

    familiar1 = padre(nombre="Gabriel", edad=56, nacimiento="1962-02-26", parentesco="Padre")
    familiar2 = madre(nombre="Susana", edad=46, nacimiento="1996-11-01", parentesco="Madre") 
    familiar3 = hermano(nombre="Agustin", edad=29, nacimiento="1991-12-09", parentesco="Hermano") 

    familiar1.save()
    familiar2.save()
    familiar3.save()

    listaFamiliares = {'familiares': [familiar1, familiar2, familiar3]}

    return render(request, 'template1.html', listaFamiliares)