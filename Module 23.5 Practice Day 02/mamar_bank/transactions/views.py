from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import EmailMultiAlternatives
from accounts.models import UserBankAccount, BankStatus
from django.db.models import Sum
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositeForm, WithdrawForm, LoanRequestForm, TransferForm
from .constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID
# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title,
        })
        return context
    
def send_transaction_mail(user, amount, subject, template, **kwargs):
    mail_subject = "Deposite Message"
    # message = render_to_string(template,{
    #     'user': user,
    #     'amount': amount,
    # })
    context = {
        'user': user,
        'amount': amount,
    }
    context.update(kwargs)
    message = render_to_string(template, context)
    send_mail = EmailMultiAlternatives(subject,'','nasrullah9867@gmail.com', to=[user.email])
    send_mail.attach_alternative(message, "text/html")
    send_mail.send()

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositeForm
    title = 'Deposite'

    def get_initial(self): # user dekhar agei form fill up krlm
        initial = {'transaction_type': DEPOSIT}
        return initial
    
    def form_valid(self, form):
        account = self.request.user.account

        bank_status = BankStatus.objects.first()
        if bank_status and bank_status.is_bankrupt:
            messages.error(self.request, "Bank is currently bankrupt. Transactions are disabled.")
            return redirect('homepage')
        
        amount = form.cleaned_data.get('amount')
        account.balance += amount # user er kase ase 500 depositted 500 so current amount is 1000
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request, f"{amount}$ was deposited to you account")
        # sending email to user when deposited
        send_transaction_mail(self.request.user, amount, "Deposite Message", "transactions/deposite_message.html")

        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw'

    def get_initial(self): # user dekhar agei form fill up krlm
        initial = {'transaction_type': WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        account = self.request.user.account
        
        bank_status = BankStatus.objects.first()
        if bank_status and bank_status.is_bankrupt:
            messages.error(self.request, "Bank is currently bankrupt. Transactions are disabled.")
            return redirect('homepage')
        
        amount = form.cleaned_data.get('amount')
        account.balance -= amount # user er kase ase 500 WITHDRAWAL 500 so current amount is 0
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request, f"Successfuly withdrawn {amount}$ from your account")
        send_transaction_mail(self.request.user, amount, "Withdrawl Message", "transactions/withdrawl_message.html")
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request Loan'

    def get_initial(self): # user dekhar agei form fill up krlm
        initial = {'transaction_type': LOAN}
        return initial
    
    def form_valid(self, form):
        bank_status = BankStatus.objects.first()
        if bank_status and bank_status.is_bankrupt:
            messages.error(self.request, "Bank is currently bankrupt. Transactions are disabled.")
            return redirect('homepage')
        
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type=3, loan_approve = True).count()
        if current_loan_count >= 3:
            return HttpResponse("Loan request crossed limits")
        messages.success(self.request, f"Successfuly loan request sent about only {amount}$")
        send_transaction_mail(self.request.user, amount, "Loan Request Message", "transactions/loan_request_message.html")
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0 # filter korar pore ba age amar total balance ke show korbe
    context_object_name = "transactions_report"

    def get_queryset(self):
        # jodi user filter na kre
        queryset = super().get_queryset().filter(account=self.request.user.account)
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

         # jodi user date filer kre
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            queryset = queryset.filter(timestamp__date__range=(start_date, end_date))

            self.balance = Transaction.objects.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
        return queryset.distinct()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context

class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, pk):
        loan = get_object_or_404(Transaction, pk=pk)

        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save()

                send_transaction_mail(self.request.user, loan.amount, "Loan Payment Message", "transactions/loan_pay_message.html")

                return redirect('loan_list')
            else:
                messages.error(request, "Insufficient balance for loan payment")
                return redirect('loan_list')

class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transactions/loan_request.html"
    context_object_name = "loans"

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account = user_account, transaction_type = LOAN)
        return queryset
    
class TransferView(LoginRequiredMixin, FormView):
    template_name = 'transactions/transfer_form.html'
    form_class = TransferForm
    success_url = reverse_lazy('transaction_report')
    
    def form_valid(self, form):
        from_account = self.request.user.account

        bank_status = BankStatus.objects.first()
        if bank_status and bank_status.is_bankrupt:
            messages.error(self.request, "Bank is currently bankrupt. Transactions are disabled.")
            return redirect('homepage')
        
        
        amount = form.cleaned_data.get('amount')
        recipient_account_no = form.cleaned_data.get('recipient_id')

        try:
            recipient_account = UserBankAccount.objects.get(account_no=recipient_account_no)
        except UserBankAccount.DoesNotExist:
            messages.error(self.request, f"Account with ID '{recipient_account_no}' not found.")
            return redirect('transfer')
        
        if from_account.balance >= amount:
            from_account.balance -= amount
            from_account.save()

            Transaction.objects.create(
                account = from_account,
                amount = amount,
                transaction_type = 5,
                balance_after_transaction = from_account.balance,
            )
            recipient_account.balance += amount
            recipient_account.save()
            Transaction.objects.create(
                account = recipient_account,
                amount = amount,
                transaction_type = 5,
                balance_after_transaction = recipient_account.balance,
            )
            messages.success(self.request, f"Transferred {amount}$ to account {recipient_account.account_no}")
            # sending email to both user when money sent
            send_transaction_mail(
                from_account.user, 
                amount, 'Send Money', 
                'transactions/send_money.html',to_username=recipient_account.user.username)
            
            send_transaction_mail(
                recipient_account.user,
                amount,
                'Money Received',
                'transactions/receive_money.html',
                to_email=recipient_account.user.email,
                from_username=from_account.user.username
            )
        else:
            messages.error(self.request, "Insufficient balance.")
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error processing your request.")
        return super().form_invalid(form)