from django.shortcuts import render, redirect
from register.forms import RegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(response, user)
            # send_mail("Registration confirmation", "You have been registered!", "fea007@inbox.ru", [form.cleaned_data.get("email")], fail_silently=False)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
