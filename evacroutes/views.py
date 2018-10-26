from django.shortcuts import render
from ussd.models import Victim
from datetime import datetime

# Create your views here.
def index(request):
    victims = Victim.objects.all()
    presenttime = datetime.now()
    return render(request, 'evacroutes/map.html', {'victims':list(victims)})

def home(request):
    return render(request, 'evacroutes/home.html')