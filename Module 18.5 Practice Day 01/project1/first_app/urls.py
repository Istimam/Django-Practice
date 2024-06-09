from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register_form, name='signup'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('passchange/', views.change_password, name='passchange'),
    path('passchangewithoutOldPass/', views.change_pass_without_old_pass, name='passchangew'),
    path('profile/', views.profile, name='profile'),
]