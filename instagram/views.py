from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate 
from .models import Image, Profile
import datetime as dt
from django.contrib.auth.models import User
from .forms import NewImageForm, SignupForm
from friendship.models import Friend, Follow, Block, FriendshipRequest
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

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
    followers = Follow.objects.followers(request.user)
    following = Follow.objects.following(request.user)
    print(images)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Instagram account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_profile = Profile.search_by_username(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "profile": searched_profile})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})