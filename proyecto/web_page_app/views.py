
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request,'index.html')


def quienes(request):
    return render(request,'quienes.html')

def servicios(request):
    return render(request,'servicios.html')

