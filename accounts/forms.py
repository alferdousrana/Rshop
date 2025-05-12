from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name',
            'phone', 'address', 'city', 'country',
            'post_code', 'profile_picture'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name',
            'phone', 'address', 'city', 'country',
            'post_code', 'profile_picture'
        )
        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'post_code']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Cory'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Anderson'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Mail@YourDomain.Com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+880 123456789'}),
            'address': forms.TextInput(attrs={'placeholder': 'Street And House Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'Your City'}),
            'country': forms.TextInput(attrs={'placeholder': 'Your Country'}),
            'post_code': forms.TextInput(attrs={'placeholder': 'Your ZIP Code'}),
        }
