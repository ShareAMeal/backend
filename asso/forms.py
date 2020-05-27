from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from api.models import Association

User = get_user_model()


class AdminCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AssoUpdateForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ['name', 'contact_email', 'location', 'description', 'phone', 'image']
