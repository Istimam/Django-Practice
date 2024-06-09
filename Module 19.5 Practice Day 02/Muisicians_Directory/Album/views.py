from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AlbumForm
from .models import Album
# Create your views here.
@method_decorator(login_required, name='dispatch')
class add_album(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')  
class edit_album(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class del_album(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)