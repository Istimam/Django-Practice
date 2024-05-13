from django.shortcuts import render
from album.models import Album
# Create your views here.
def home(request):
    data = Album.objects.all()
    # print(data)
    return render(request, 'home.html',{'data':data})