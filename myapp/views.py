from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about.html')
