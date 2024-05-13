from django.shortcuts import render
from . forms import ApplicationForm
from . import models
# Create your views here.

def home(request):
    return render(request,'home.html')

def DjangoForm(request):
    form = ApplicationForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'form.html', {'form': form})
def Table(request):
    User = models.User.objects.all()
    print(User)
    return render(request,'table.html',{'Users': User})