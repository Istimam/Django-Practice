from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up/', views.SignupForm.as_view(), name='sign_up'),
    path('login/', views.Loginview.as_view(), name='login'),
    path('logout/', views.Logoutview, name='logout'),
]