from django import forms
from .models import Order


class PaymentForm(forms.Form):
    """
        Creating the fields for the Stripe
        Payment Form.
    """
    MONTHS = [(i, i) for i in range(1, 13)]
    YEARS = [(i, i) for i in range(2019, 2026)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTHS, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEARS, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
        Order Form for Stripe 
        details.
    """
    class Meta:
        model = Order
        fields = ()
