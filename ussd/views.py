from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


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
            response = "Your response has been recorded.\n"
            response += "A relief team will soon approach you" 
        return HttpResponse(response)
    else:
        return HttpResponse("Response can't be made")