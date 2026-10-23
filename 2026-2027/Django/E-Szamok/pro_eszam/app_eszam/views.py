from django.http import HttpResponse
from django.shortcuts import render
from .models import Adalek, Funkcio

from django.db.models import Count


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

## TODO: 4szeles
def view_4szeles(request):
    leggyakoribb = (
    Funkcio.objects.values('kod')
    .annotate(occurences=Count('kod'))
    .order_by('-occurences')
    .first()
    )

    funkcioi = leggyakoribb['occurences']
    most_common = leggyakoribb['kod']

    context = {
        'most_common' : most_common,
        'funkcioi' : funkcioi,
    }
    return render(request, '4szeles.html', context)

def view_5multi(request):
    legalabb_50 = (
        Funkcio.objects.values('fnev')
        .annotate(adalek_szam=Count('kod'))
        .filter(adalek_szam__gte=50)
        .values_list('fnev', flat=True)
    )

    context = {
        'data': legalabb_50,
    }

    return render(request, '5multi.html', context)

def view_6kopott(request):
    possible_adalekok = Adalek.objects.filter(nev__icontains = "sav").values_list('kod')
    possbile_kodok = Funkcio.objects.filter(kod__in=possible_adalekok, fnev__icontains = "anti").values_list('kod', flat=True)

    context = {
        'possibles' : possbile_kodok
    }

    return render(request, '6kopott.html', context)

def view_7stat(request):
    adatok = (
        Funkcio.objects.values('fnev')
        .annotate(darabszam=Count('kod'))
        .order_by('-darabszam')
    )
    
    context = {
        'adatok': adatok
    }
    return render(request, '7stat.html', context)