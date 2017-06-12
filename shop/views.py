from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    articles = Artikel.objects.all().order_by('-npreis')
    return render(request, 'index.html', {'artikel': articles})

def details(request, aid):
    a = Artikel.objects.filter(anr=aid)[0]
    f = Feedback.objects.filter(bestellartikel__artikel__anr=aid)
    return render(request, 'details.html', {'artikel': a, 'feedback': f})

