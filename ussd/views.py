from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .utilities.SMS import SMS
from .models import Victim, Volunteer
from evacroutes.models import Update
import requests

@csrf_exempt
def ussdrelief(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        
        volunteer = Volunteer.objects.filter(phone_number=phone_number)
        if(volunteer):
            if text == "":
                response = "CON What do you want to do\n"
                response += "1. Show Victims\n"
                response += "2. Send an alert\n"
                response += "3. Show Volunteer/Shelter locations\n"

            elif text == "1":
                #TODO: Add the code needed to show the victims here
                volunteer=list(volunteer)[0]
                query="SELECT *, COUNT(*) AS count FROM ussd_victim GROUP BY location"
                victims=Victim.objects.raw(query)
                victims=list(victims)
                for i in range(len(victims)):
                    response+=victims[i].location+" "+str(victims[i].count)+"\n"

            elif text == "2":
                response = "END Send the alert via SMS to\n"
                response+="86387 as\n"
                response+="ALERT <text>"

            elif text == "3":
                volunteers = Volunteer.objects.all()
                volunteers = list(volunteers)
                response += "END"
                for i in range(len(volunteers)):
                    response += str(i+1)+". "+volunteers[i].location+"\n"
            elif text == "4":
                response = "END asjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdvasjdfcnadcakjsdbckajjsdbcjbasdbakjsbdv"

        else:
            response = "END Please send the nearest\n"
            response += "landmark to 86387 via SMS\n"
            response += "along with your pincode"

        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")

@csrf_exempt
def sms(request):
    if request.method == 'POST':
        fro = request.POST.get('from')
        to = request.POST.get('to')
        text = request.POST.get('text')
        date = request.POST.get('date')
        id = request.POST.get('id')
        print(to)
        query=text.replace(' ', '%20')
        key='Aqxws6GyR0KaQH-uo9w92nqNeePHAzsbkVDbrpiayIiAwfTbXcML-wj1XLEBPQcQ'
        url='http://dev.virtualearth.net/REST/v1/Locations?q='+query+'&o=json&key='+key
        result=requests.get(url)
        result=result.json()
        lat,lon=result['resourceSets'][0]['resources'][0]['point']['coordinates']
        if to=="86386":
            victim=Victim(phone_number=fro,lat=lat,lon=lon,rescued=True)
            victim.save()
        elif to=="86387" and text[:5]=="ALERT":
            victims=Victim.objects.exclude(phone_number=fro)
            recipients=["+"+str(victim.phone_number) for victim in list(victims)]
            volunteers=Volunteer.objects.exclude(phone_number=fro)
            recipients.extend(["+"+str(volunteers.phone_number) for volunteer in list(volunteers)])
            message=text[6:]
            SMS().send_sms_sync(recipients=recipients,message=str(message))
        elif to=="86387":
            volunteer=Volunteer(phone_number=fro,lat=lat,lon=lon,location=text)
            volunteer.save()
        return HttpResponse("Success")

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
                response += "2. Get Updates\n"
                response += "3. Send info to all people"

            elif text == "1":
                print(list(victim)[0].rescued)
                list(victim)[0].setRescued(False)
                print(list(victim)[0].rescued)
                list(victim)[0].save()
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
            elif text == "3":
                response = "END Send the alert via SMS to\n"
                response+="86387 as\n"
                response+="ALERT <text>"

        else:
            response = "END Please send the nearest\n"
            response += "landmark to 86386 via SMS\n"
            response += "along with your pincode"

        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")
