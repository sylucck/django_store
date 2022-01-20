from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    phone=forms.CharField(max_length=15)
    amount = forms.FloatField()
