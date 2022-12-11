from django.shortcuts import render, redirect
from authentication import forms
from django.contrib.auth import login, logout
from django.conf import settings

# Create your views here.
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form':form})

def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)