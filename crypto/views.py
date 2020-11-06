from django.http import HttpResponse

from .models import Crypto


def index(request):
    crypto_list = Crypto.objects.order.all
    output = ', '.join([q.name for q in crypto_list])
    return HttpResponse(output)
