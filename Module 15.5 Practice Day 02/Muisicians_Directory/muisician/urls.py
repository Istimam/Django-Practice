from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_muisician, name='add_muisician'),
    path('edit/<int:id>', views.edit_muisician, name='edit_muisician'),
    path('delete/<int:id>', views.delete_muisician, name='delete_muisician'),
]