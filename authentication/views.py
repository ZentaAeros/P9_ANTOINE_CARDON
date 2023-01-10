from django.shortcuts import render, redirect
from authentication import forms
from django.contrib.auth import login, logout
from django.conf import settings
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from authentication.models import User, UserFollows

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

@login_required
def follow_user(request):
    form = forms.SearchUser()
    if request.method == 'POST':
        form = forms.SearchUser(request.POST)
        if form.is_valid():
            try:
                followed_user = User.objects.get(username=request.POST['user'])
                if request.user == followed_user:
                    messages.error(request, 'Vous ne pouvez pas vous suivre')
                else:
                    try:
                        UserFollows.objects.create(user=request.user, followed_user=followed_user)
                        messages.success(request, f'Vous suivez désormais {followed_user}')
                    except IntegrityError:
                        messages.error(request, f'Vous suivez déjà {followed_user}')
            except User.DoesNotExist:
                messages.error(request, f'L\'utilisateur n\'existe pas.')
    user_follow = UserFollows.objects.filter(user=request.user).order_by('followed_user')
    followed = UserFollows.objects.filter(followed_user=request.user).order_by('user')
    actual_user = request.user
    context = {
        'user_follow':user_follow,
        'followed':followed,
        'actual_user':actual_user,
        'form':form
    }
    return render(request, 'authentication/followed_user.html', context)

@login_required
def unfollow_user(request, id):
    user_to_unfollow = User.objects.get(id=id)
    if request.method == 'POST':
        unfollow = UserFollows.objects.filter(followed_user=user_to_unfollow)
        unfollow.delete()
        return redirect('followers')
    return render(request, 'authentication/unfollow_user.html', context={'user_to_unfollow':user_to_unfollow})