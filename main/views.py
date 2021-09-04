from django.shortcuts import render
from .models import Ticker


def index(request):
    ticker = Ticker.objects.first()
    return render(request, "main/index.html", {"ticker": ticker})


# Create your views here.
