from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission


# Create your views here.

def prepare_permissions():
    objs = Permission.objects.filter(id=id).update(codename="view_movie")

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, "registration/signup.html", {
        'form': form
    })          