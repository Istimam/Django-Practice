from django.urls import path, include
from . import views

urlpatterns = [
    path('add_muisician/', views.add_muisician.as_view(), name='add_muisician'),
    path('edit_muisician/<int:pk>/', views.edit_muisician.as_view(), name='edit_muisician'),
]