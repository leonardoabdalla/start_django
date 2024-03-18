from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def newapp(request):
    return render(request, 'galeria/newapp.html')
