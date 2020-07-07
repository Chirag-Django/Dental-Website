from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == 'POST':
        subject = 'Thank you for registering to our site'
        message_to_user = ' it  means a world to us '
        message_name = request.POST['message-name']
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message_to_user,
            email_from,
            [request.POST['message-email']],
            fail_silently=False,
        )
        return render(request,'contact.html',{'message_name':message_name})
    return render(request,'contact.html',{})