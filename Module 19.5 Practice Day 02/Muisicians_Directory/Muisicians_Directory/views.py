from django.shortcuts import render
from Album.models import Album
def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'albums': data})