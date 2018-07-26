from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
import datetime as dt
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    image = Image.get_all()

    return render(request, 'index.html', {"image":image})

def logout(request):
    logout(request)
    return render(request, 'login.html')