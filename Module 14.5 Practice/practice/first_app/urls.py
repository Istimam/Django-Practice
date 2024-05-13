from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('form/', views.DjangoForm, name='formPage'),
    path('table/', views.Table, name='tablePage'),
]
