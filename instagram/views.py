from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
import datetime as dt
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import NewImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    
    date = dt.date.today()
    image = Image.get_all()
    return render(request, 'index.html', locals())

def logout(request):
    logout(request)
    return render(request, 'login.html')

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = current_user
            image.save()
            return redirect ('index')
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
        date = dt.date.today()
        my_profile = User.objects.get(id =user_id)
        return render(request, 'profile.html', locals())


def images_profile(request, id):
    current_user = User.objects.filter(id=id).first()
    profile = current_user.profile
    details=Profile.get_by_id(id)
    images=Image.objects.filter(user_id=request.user.id)
    # images = Images.get_profile_images(id)
    print(images)
    return render(request, 'profile.html', locals())
