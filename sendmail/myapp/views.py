from django.shortcuts import render 
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == 'POST':
        message=request.POST['message']
        email=request.POST['email']
        name=request.POST['name']
        send_mail(
            'Contact_info',#title
            message,#message
            'settings.EMAIL_HOST_USER',
            [''], #custormers list whom u want to sent it..
            fail_silently=False)         
        
        
    return render(request,'index.html')