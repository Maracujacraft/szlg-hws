from django.http import HttpResponse
from django.shortcuts import render
from .models import Adalek, Funkcio



# Create your views here.



def view_import(request):
    return render(request, 'import.html', {})

def view_import_kuld(request):
    

    if  request.method!="POST":
        return HttpResponse("Nem jól küldted el a formot ('Küldés' gomb)")

    szotar = request.POST

    if 'adalekok' not in szotar:
        return HttpResponse("Valami nem jó az űrlappal... (adalekok)")
    if 'funkciok' not in szotar:
        return HttpResponse("Valami nem jó az űrlappal... (funkciok)")
    
    adal_input_str = szotar['adalekok']
    funk_input_str = szotar['funkciok']
    ## Innentől kezdve ez egy mezei python feladat

    print(adal_input_str + " " + funk_input_str)


    adal_sorok = adal_input_str.strip().split('\n')
    adaldb = -1
    for sor in adal_sorok:
        sortomb = sor.strip().split('\t')
        if adaldb != -1:
            adalek, is_created = Adalek.objects.get_or_create(kod=int(sortomb[0]), nev=sortomb[1], mellekhatas=sortomb[2])
            if is_created:
                adaldb+=1
        else:
            adaldb+=1
    
    funk_sorok = adal_input_str.strip().split('\n')
    funkdb = -1
    for sor in funk_sorok:
        sortomb = sor.strip().split('\t')
        if funkdb != -1:
            funkcio, is_created = Funkcio.objects.get_or_create(kod=int(sortomb[0]), nev=sortomb[1], mellekhatas=sortomb[2])
            if is_created:
                funkdb+=1
        else:
            funkdb+=1

    return render(request, 'app_hetedik/import_kesz.html', {'adaldb': adaldb, 'funkdb': funkdb})




    # todo: no az