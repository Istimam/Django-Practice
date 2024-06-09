from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def register_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('profile')
        else:
            register_form = RegisterForm()
        return render(request,'signup.html',{'form':register_form})
    else:
        return redirect('profile')
def loginform(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['username']
                userpass = login_form.cleaned_data['password']
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    messages.success(request, 'Looged in successfully')
                    login(request,user)
                    return redirect('profile')
        else:
            login_form = AuthenticationForm()
        return render(request,'login.html',{'form':login_form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
        return redirect('login')

def user_logout(request):
    messages.warning(request, 'Looged out successfully')
    logout(request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            change_form = PasswordChangeForm(data=request.POST, user=request.user)
            if change_form.is_valid():
                change_form.save()
                update_session_auth_hash(request,change_form.user)
                return redirect('profile')
        else:
            change_form = PasswordChangeForm(user=request.user)
        return render(request,'change_pass.html',{'form':change_form})
    else:
        return redirect('login')
def change_pass_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            change_form = SetPasswordForm(data=request.POST, user=request.user)
            if change_form.is_valid():
                change_form.save()
                update_session_auth_hash(request,change_form.user)
                return redirect('profile')
        else:
            change_form = SetPasswordForm(user=request.user)
        return render(request,'change_pass.html',{'form':change_form})
    else:
        return redirect('login')