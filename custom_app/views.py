from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_app.models import BaseUser
from django.contrib.auth import login, logout, authenticate
from custom_app.forms import SignupForm, LoginForm
from custom_user.settings import AUTH_USER_MODEL

def index(request):
    my_user = BaseUser.objects.all()
    return render(request, "index.html", {'my_user': my_user, "output": AUTH_USER_MODEL})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = BaseUser.objects.create_user(username=data.get("username"), password=data.get("password"), display_name=data.get("display_name"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("home"))
    
    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))

    form = LoginForm()
    return render(request,  "generic_form.html", {"form": form} )

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))