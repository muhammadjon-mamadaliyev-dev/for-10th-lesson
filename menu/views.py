
from django.shortcuts import render
from .models import Taom

def index(request):
    asosiy = Taom.objects.filter(kategoriyasi = 'Asosiy taomlar')
    salat = Taom.objects.filter(kategoriyasi='Salatlar')
    shirinlik = Taom.objects.filter(kategoriyasi='Shirinliklar')
    ichimlik = Taom.objects.filter(kategoriyasi='Ichimliklar')

    taomlar = []


    if asosiy:
        taomlar.append(
            {
                'turi':'Asosiy taomlar',
                'taomlar':asosiy

            }
        )
    if salat:
        taomlar.append(
            {
                'turi':'Salatlar',
                'taomlar':salat

            }
        )
    if shirinlik:
        taomlar.append(
            {
                'turi':'Shirinliklar',
                'taomlar':shirinlik

            }
        )
    if ichimlik:
        taomlar.append(
            {
                'turi':'Ichimliklar',
                'taomlar':ichimlik

            }
        )
    return render(request, 'menu/index.html', {'taomlar': taomlar,'tab':'Barcha Taomlar'})


def kategoriya(request):
    k = request.GET.get('k')
    natija = Taom.objects.filter(kategoriyasi=k)

    taomlar = []  
    taomlar.append({
        'turi': k,
        'taomlar': natija
    })

    return render(request, 'menu/index.html', {'taomlar': taomlar, 'tab': k})
    return render(request ,"meal/index.html")
