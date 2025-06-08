from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is about')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is services')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # email = request.POST.get('email')
        contact= Contact (name= name,date= datetime.today() )
        contact.save()
    return render (request, 'contact.html')
    #return HttpResponse('this is contact')