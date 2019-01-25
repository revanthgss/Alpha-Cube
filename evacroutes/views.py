from django.shortcuts import render
from django.http import HttpResponse
from ussd.models import Victim
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Update

# Create your views here.
def index(request):
    victims = Victim.objects.filter(rescued=False)
    return render(request, 'evacroutes/map.html', {'victims':list(victims)})

def home(request):
    return render(request, 'evacroutes/home.html')

def form(request):
    return render(request, 'evacroutes/form.html')

@csrf_exempt
def post(request):
    if request.method == 'POST':
        u = request.POST.get('update')
        update = Update(message = u)
        update.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Fail")

def about(request):
    return render(request, 'evacroutes/about.html')


def data(request):
    victims = []
    victims = Victim.objects.all()
    return render(request, 'evacroutes/display.html', {'victims': victims})