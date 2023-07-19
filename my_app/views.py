from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from my_app.models import Dostavka



def hole_product(request):
    products = Dostavka.objects.all().order_by('-id')

    context = {
        'products':products,
    }

    return render(request, "hole_product.html", context)



def completed_product(request):
    products = Dostavka.objects.filter(status='yetkazib_berilgan').order_by('-id')

    context = {
        'products':products,
    }

    return render(request, "completed_product.html", context)


def waiting_product(request):
    products = Dostavka.objects.filter(status='tayyorlanmoqda').order_by('-id')

    context = {
        'products':products,
    }

    return render(request, "waiting_product.html", context)




