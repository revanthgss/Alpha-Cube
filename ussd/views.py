from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Victim
import random
from shapely.geometry import Point,Polygon

def generate_random():
    polygon = Polygon([(8.336403, 77.151127), (11.064461, 76.700373), (11.952782, 75.806202)])
    minx, miny, maxx, maxy = polygon.bounds
    while True:
        pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(pnt):
            return pnt.x,pnt.y

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        
        if text == "":
            response = "CON What do you want to do \n"
            response += "1. Ask for support\n"
            response += "2. Get Updates"


        elif text == "1":
            lat,lon = generate_random()
            victim = Victim(phone_number=phone_number, lat=lat, lon=lon)
            victim.save()
            response = "END Your response has been recorded.\n"
            response += "A relief team will soon approach you" 
        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")