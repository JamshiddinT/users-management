from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'email', 'username']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'username']


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.status == 'BLOCKED':
            raise forms.ValidationError("Your account is blocked. Please contact support.")
