from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Victim
from evacroutes.models import Update
import requests

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        
        victim = Victim.objects.filter(phone_number=phone_number)
        if(victim):
            if text == "":
                response = "CON What do you want to do\n"
                response += "1. Ask for support\n"
                response += "2. Get Updates"

            elif text == "1":
                response = "END Your response has been recorded\n"
                response += "A response team will soon\n"
                response += "approach you."

            elif text == "2":
                updates = Update.objects.order_by('time')
                updateslist = list(updates)
                response = "END 1. "
                response += updateslist[len(updateslist)-1].message
                if(len(updateslist)>1):
                    response += "\n 2. "+updateslist[len(updateslist)-2].message

        else:
            response = "END Please send the nearest\n"
            response += "landmark to 83626 via SMS\n"
            response += "along with your pincode"

        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")

@csrf_exempt
def sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('from')
        to = request.POST.get('to')
        text = request.POST.get('text')
        date = request.POST.get('date')
        id = request.POST.get('id')

        query=text.replace(' ', '%20')
        key='Aqxws6GyR0KaQH-uo9w92nqNeePHAzsbkVDbrpiayIiAwfTbXcML-wj1XLEBPQcQ'
        url='http://dev.virtualearth.net/REST/v1/Locations?q='+query+'&o=json&key='+key
        result=requests.get(url)
        result=result.json()
        lat,lon=result['resourceSets'][0]['resources'][0]['point']['coordinates']
        victim=Victim(phone_number=phone_number,lat=lat,lon=lon)
        victim.save()
        return HttpResponse("Success")