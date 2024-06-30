from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView, UserPasswordChangeView, UserProfileView

urlpatterns = [
path('register/', UserRegistrationView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('profile/', UserProfileView.as_view(), name='profile'),
path('updateProfile/', UserBankAccountUpdateView.as_view(), name='updateProfile'),
path('password-change/', UserPasswordChangeView.as_view(), name='password'),
path('logout/', UserLogoutView.as_view(), name='logout'),
]