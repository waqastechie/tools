from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from email_validator.models import EmailValidator
# Create your views here.


def index(request):

    return render(request, "email-validator-index.html")


def email_validator(request):
    if request.POST.get('email', None) is not None:
        email_address = request.POST.get('email')
        email_obj = EmailValidator.objects.filter(
            email=email_address
        )
        response = {}
        print(email_obj)
        if not email_obj:

            res = requests.get(
                "https://isitarealemail.com/api/email/validate",
                params={'email': email_address})
            status = res.json()['status']
            if status == "valid":
                response["email"] = email_address
                response["status"] = status
                email_validator_obj = EmailValidator(
                    email=email_address)
                email_validator_obj.save()
            elif status == "invalid":
                response["email"] = email_address
                response["status"] = status

            else:
                response["email"] = email_address
                response["status"] = status

        else:
            
            response["email"] = email_address
            response["status"] = "valid"
            print(response)
        return render(request, "email-validator-index.html", {"response": response})
    return redirect('email_validator_index')
