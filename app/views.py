from django.shortcuts import render

# Create your views here.
def index(request):
    if request.headers.get("HX-Request") == "true":
        return render(request, 'partials/index.html')
    else:
        return render(request, 'index.html')