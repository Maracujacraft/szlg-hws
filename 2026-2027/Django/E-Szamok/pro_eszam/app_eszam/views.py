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

    print(adal_input_str + "\n\n\n\n\n\n\n" + funk_input_str+"\n\n\n")


    adal_sorok = adal_input_str.splitlines()
    adaldb = 0
    for asor in adal_sorok[1:]:
        sortomb = [mezo.strip() for mezo in asor.split('\t')]
        if len(sortomb) != 3:
            return HttpResponse(f"Hibás funkciósor: {asor!r}")
        adalek, is_created = Adalek.objects.get_or_create(kod=str(sortomb[0]), nev=str(sortomb[1]), mellekhatas=bool(sortomb[2]))
        if is_created:
            adaldb+=1
    
    funk_sorok = funk_input_str.splitlines()
    funkdb = 0
    for fsor in funk_sorok[1:]:
        sortomb = [mezo.strip() for mezo in fsor.split('\t')]
        if len(sortomb) != 2:
            return HttpResponse(f"Hibás funkciósor: {fsor!r}")
        funkcio, is_created = Funkcio.objects.get_or_create(kod=str(sortomb[0]), fnev=str(sortomb[1]))
        if is_created:
            funkdb += 1

    return render(request, 'import_success.html', {'adaldb': adaldb, 'funkdb': funkdb})


def view_index(request):
    return render(request, 'index.html')

def view_2kerulendo(request):
    mellekhatasosok = Adalek.objects.filter(mellekhatas=True).order_by('nev')
    
    context = {
        'mellekhatasosok': mellekhatasosok
    }
    return render(request, '2kerulendo.html', context)

def view_3karamell(request):
    karamell_kodok = Adalek.objects.filter(nev__icontains="karamell").values_list('kod')
    karamellesek = Funkcio.objects.filter(kod__in=karamell_kodok)

    context = {
        'karamellesek': karamellesek
    }
    return render(request, '3karamell.html', context)
