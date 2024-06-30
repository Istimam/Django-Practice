from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views.generic import FormView
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, CustomPasswordChangeForm
from django.core.mail import send_mail
from .models import UserBankAccount
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik tha ke

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    
class UserLogoutView(LogoutView):
    next_page = 'homepage'

    def get(self, request, *args, **kwargs):
        # Custom logout logic can be added here if needed
        if self.request.user.is_authenticated:
            response = super().get(request, *args, **kwargs)
            return response
        
class UserProfileView(View):
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(instance=request.user)
        password_change_form = CustomPasswordChangeForm(user=request.user)

        context = {
            'user_update_form': user_update_form,
            'password_change_form': password_change_form,
        }
        return render(request, self.template_name, context)     


class UserBankAccountUpdateView(View):
    template_name = 'accounts/update_profile.html'

    def get(self, request):
        user = request.user
        user_bank_account = UserBankAccount.objects.get(user=user)
        form = UserUpdateForm(instance=request.user)
        context = {
            'form': form,
            'user_bank_account': user_bank_account,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        user_bank_account = UserBankAccount.objects.get(user=user)

        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

        context = {
            'form': form,
            'user_bank_account': user_bank_account,
        }
        return render(request, self.template_name, context)

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/pass_change.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password has been changed successfully.')
        # Send email after password change successfull
        mail_subject = "Password Changed Successfully"
        message = render_to_string('accounts/pass_change_message.html', {
            'user' : self.request.user
        })
        to_email = self.request.user.email
        send_email = EmailMultiAlternatives(mail_subject, '','nasrullah9867@gmail.com', to = [to_email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)