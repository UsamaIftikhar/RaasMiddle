from django import forms
from django.forms import PasswordInput

from .models import *


class UserForm(forms.ModelForm):

    class Meta:
        model= userInfo
        fields = [
            # 'firstName',
            # 'lastName',
            'email',
            'password',
            # 'age',
            # 'address',
            # 'phoneNumber'
        ]
        widgets = {
            # 'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': 'autofocus'}),
            # 'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            # 'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
        }
        labels = {
            # 'firstName': 'First Name',
            # 'lastName': 'Last Name',
            'email': 'Email',
            'password': 'Password',
            # 'image': 'Image',
            # 'address': 'Address',
            # 'phoneNumber': 'Phone Number'
        }


class AppForm(forms.ModelForm):

    class Meta:
        model = addapps
        fields = [
            # 'firstName',
            'app_id',
            'appname',
            'webaddress',
             'user_id',
            # 'age',
            # 'address',
            # 'phoneNumber'
        ]
        widgets = {
            # 'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': 'autofocus'}),
            'app_id': forms.HiddenInput(),
            'appname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AppName'}),
            'webaddress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WebAddress'}),
             'user_id': forms.HiddenInput(),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            # 'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
        }
        labels = {
            # 'firstName': 'First Name',
            # 'lastName': 'Last Name',
            'appname': 'AppName',
            'webaddress': 'WebAddress',
             'user_id': 'UserId',
            # 'image': 'Image',
            # 'address': 'Address',
            # 'phoneNumber': 'Phone Number'
        }

class CompanyForm(forms.ModelForm):

    class Meta:
        model= company
        fields = [
            # 'firstName',
            # 'lastName',
            'company_id',
            'email',
            'password',
            # 'age',
            # 'address',
            # 'phoneNumber'
        ]
        widgets = {
            # 'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': 'autofocus'}),
            # 'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'company_id': forms.HiddenInput(),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            # 'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
        }
        labels = {
            # 'firstName': 'First Name',
            # 'lastName': 'Last Name',
            'email': 'Email',
            'password': 'Password',
            # 'image': 'Image',
            # 'address': 'Address',
            # 'phoneNumber': 'Phone Number'
        }


class NewAppForm(forms.ModelForm):

    class Meta:
        model = APP
        fields = [
            # 'firstName',
            'app_id',
            'appname',
            'webaddress',
             'company_id',
            # 'age',
            # 'address',
            # 'phoneNumber'
        ]
        widgets = {
            # 'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': 'autofocus'}),
            'app_id': forms.HiddenInput(),
            'appname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AppName'}),
            'webaddress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WebAddress'}),
             'company_id': forms.HiddenInput(),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            # 'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
        }
        labels = {
            # 'firstName': 'First Name',
            # 'lastName': 'Last Name',
            'appname': 'AppName',
            'webaddress': 'WebAddress',
             'user_id': 'UserId',
            # 'image': 'Image',
            # 'address': 'Address',
            # 'phoneNumber': 'Phone Number'
        }
