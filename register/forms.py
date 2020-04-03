from django import forms
from django.contrib.auth.forms import UserCreationForm

#On recupere le model User cree dans api (Premier endroit où ça a été ecrit)
from django.contrib.auth import get_user_model
User = get_user_model()

#Classe pour le form d'inscription
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

#Classe pour le form de connexion
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class CreerAsso(forms.Form):
    contact_email = forms.EmailField()
    name = forms.CharField()
    location = forms.CharField()
    description = forms.CharField()
    phone = forms.CharField()