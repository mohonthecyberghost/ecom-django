from django.shortcuts import render

from eshopadmin.models import product


def index(request):
    test = product.objects.all()
    cotext = {
        'test': test
    }
    return render(request, 'eshopview/home.html', cotext)

def cartCheck(request):

    return render(request, 'eshopview/home.html')

