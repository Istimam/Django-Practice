from django.urls import path, include
from . import views

urlpatterns = [
    path('add_album/', views.add_album.as_view(), name='add_album'),
    path('edit_album/<int:pk>/', views.edit_album.as_view(), name='edit_album'),
    path('del_album/<int:pk>/', views.del_album.as_view(), name='del_album'),
]