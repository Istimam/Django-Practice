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

# @method_decorator(login_required, name='dispatch')
# class Logoutview(LogoutView):
#     def get_success_url(self):
#         return reverse_lazy('homepage')
#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         messages.success(request, 'You have been logged out successfully.')
#         return response
    

def Logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

