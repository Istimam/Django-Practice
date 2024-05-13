from django import forms
from django.forms.widgets import NumberInput, datetime

# Create your forms here.
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=50, initial='Your Full Name')
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=13)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    weight = forms.DecimalField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label="Tell Us About Yourself",max_length= 100)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    agree = forms.BooleanField(label="I Agree")
    day = forms.DateField(initial=datetime.date.today, label="Submission Day")
