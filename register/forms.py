from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

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
    contact_email = forms.EmailField(label="Email")
    name = forms.CharField(label="Nom de l'association",max_length=127)
    location = forms.CharField(label="Adresse",max_length=1023)
    description = forms.CharField(label="Description")
    phone = forms.CharField(label="Telephone",max_length=15)

class CreerEvent(forms.Form):
    name = forms.CharField(label="Nom", max_length=63)
    start_datetime = forms.DateTimeField(label="Date de début")
    start_datetime.initial=timezone.now
    active = forms.BooleanField(label="Évènement non fini")
    active.required = False
    description = forms.CharField(label="Description")

