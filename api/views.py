from django.shortcuts import render
from api.models import *
# Create your views here.

def index(request):
    generation = Generation.objects.all()
    return render(request, 'index.html')
