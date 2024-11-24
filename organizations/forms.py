from django import forms
from .models import CustomUser, Organization

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'organization']
