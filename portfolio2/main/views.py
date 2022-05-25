from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Contact
# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def sendContact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.email = request.POST.get('email')
        contact.number_of_telephone = request.POST.get('number')
        contact.message = request.POST.get('message')
        contact.save()

        return HttpResponseRedirect('/')