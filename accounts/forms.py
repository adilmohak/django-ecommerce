from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Username", )

    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="First Name", )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Last Name", )

    address = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Address", )

    phone = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Mobile No.", )

    email = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Email", )

    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password", )

    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Password Confirmation", )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class ProfileUpdateForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', }),
        label="Email Address", )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="First Name", )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Last Name", )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Phone No.", )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Address / city", )

    class Meta:
        model = User
        fields = ['email', 'phone', 'address', 'picture', 'first_name', 'last_name']


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "There is no user registered with the specified E-mail address. "
            self.add_error('email', msg)
            return email
# ###########################################################
