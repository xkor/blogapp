from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, logout, login


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                phone_number=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('posts_list_url')
    return render(request, 'uauth/login.html')


def logout_view(request):
    logout(request)
    print(request.user)
    return redirect('posts_list_url')
