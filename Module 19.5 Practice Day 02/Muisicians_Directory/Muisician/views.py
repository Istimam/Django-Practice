from django.shortcuts import render, redirect
from . import forms
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Muisician
from django.urls import reverse_lazy
# Create your views here.
class add_muisician(CreateView):
    model = Muisician
    form_class = forms.MuisicianForm
    template_name = 'add_muisician.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        return super().form_valid(form)
    
class edit_muisician(UpdateView):
    model = Muisician
    form_class = forms.MuisicianForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('homepage')