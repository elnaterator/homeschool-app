from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')