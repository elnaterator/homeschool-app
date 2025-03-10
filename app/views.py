from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .utils import html_response
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    # check if user is authenticated
    if request.user.is_authenticated:
        logger.info(f"User {request.user} is authenticated")
        return html_response("home", request)
    else:
        logger.info("User is not authenticated")
        return redirect('login')
        

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"User {username} logged in successfully")
                return redirect('home')
            else:
                logger.warning(f"Failed login attempt for user {username}")
        else:
            logger.warning("Invalid login form submission: %s", form.errors)
    else:
        form = AuthenticationForm()
    return html_response("auth", request, {
        'form_type': 'login', 
        'form': form, 
        'errors': form.errors.as_text(),
        'non_field_errors': form.non_field_errors()
    })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f"New user {user.username} signed up and logged in successfully")
            return redirect('home')
        else:
            logger.warning("Invalid signup form submission")
    else:
        form = UserCreationForm()
    return render(request, 'auth/_auth_form.html', {'form': form, 'form_type': 'signup'})

def logout_view(request):
    logout(request)
    return redirect('login')