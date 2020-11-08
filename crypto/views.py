import requests
from django.shortcuts import render

from .models import Crypto


def index(request):
    cryptos = Crypto.objects.all()
    print(cryptos)

    context = {}

    return render(request, 'index.html', context)

