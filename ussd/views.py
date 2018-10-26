from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Victim
import random

LAT_END = 11260864
LAT_START = 8682914
LON_START = 75782874
LON_END = 76948055

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
            lat=(random.randint(LAT_START,LAT_END))/1000000
            lon=(random.randint(LON_START,LON_END))/1000000
            victim = Victim(phone_number=phone_number, lat=lat, lon=lon)
            victim.save()
            response = "END Your response has been recorded.\n"
            response += "A relief team will soon approach you" 
        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")