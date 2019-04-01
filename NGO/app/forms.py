from django import forms
from phone_field import PhoneField


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = forms.CharField(label='Address', max_length=100)
    adultQty = forms.CharField(label='Adult Quantity', max_length=2)
    childQty = forms.CharField(label='Child Quantity', max_length=2)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


