from django.shortcuts import render
from api.models import *
import json
# Create your views here.

def index(request):
    generation = Generation.objects.all()
    json = request.POST.get('192.168.30.199:9090')
    json = json.json()
    print(json)
    return render(request, 'index.html')
