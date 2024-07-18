from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def contacts(request):
    return render(request,'contacts.html')

def placement(request):
    return render(request,'placement.html')
