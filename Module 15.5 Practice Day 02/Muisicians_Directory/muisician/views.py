from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def add_muisician(request):
    if request.method == 'POST':
        muisician_form = forms.MuisicianForm(request.POST)
        if muisician_form.is_valid():
            muisician_form.save(commit=True)
            return redirect('homepage')
    else:
        muisician_form = forms.MuisicianForm()
    return render(request, 'add_muisician.html', {'form': muisician_form})
def edit_muisician(request, id):
    muisician = models.Muisician.objects.get(pk=id)
    muisician_form = forms.MuisicianForm(instance=muisician)
    if request.method == 'POST':
        muisician_form = forms.MuisicianForm(request.POST, instance=muisician)
        if muisician_form.is_valid():
            muisician_form.save(commit=True)
            return redirect('homepage')
    return render(request, 'add_muisician.html', {'form': muisician_form})

def delete_muisician(request, id):
    muisician = models.Muisician.objects.get(pk=id)
    muisician.delete()
    return redirect('homepage')