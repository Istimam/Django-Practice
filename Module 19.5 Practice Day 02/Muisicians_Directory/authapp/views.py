from . import forms
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
# Create your views here.
class SignupForm(CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        messages.success(self.request, 'Account Created Successfully')
        return valid
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information is invalid')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Signup'
        return context

    
class Loginview(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information is invalid')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# class Logoutview(LogoutView):
#     template_name = 'logout.html'
#     login_url = 'login'
#     def post(self,request, *args, **kwargs):
#         logout(request)
#         messages.add_message(request, messages.SUCCESS, 'You have been logged out successfully.')
#         return HttpResponseRedirect(reverse_lazy('login'))

def Logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

