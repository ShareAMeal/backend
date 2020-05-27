from django import forms
# On recupere le model User cree dans api (Premier endroit où ça a été ecrit)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


# Classe pour le form d'inscription
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Classe pour le form de connexion
class ConnexionForm(forms.Form):
    username = forms.CharField(label=_("Nom d'utilisateur"), max_length=30)
    password = forms.CharField(label=_("Mot de passe"), widget=forms.PasswordInput)


class CreerAsso(forms.Form):
    contact_email = forms.EmailField(label=_("Email"))
    name = forms.CharField(label=_("Nom de l'association"), max_length=127)
    location = forms.CharField(label=_("Adresse"), max_length=1023)
    description = forms.CharField(label=_("Description"))
    phone = forms.CharField(label=_("Telephone"), max_length=15)


class CreerEvent(forms.Form):
    name = forms.CharField(label="Nom", max_length=63)
    start_datetime = forms.DateTimeField(label=_("Date de début"))
    start_datetime.initial = timezone.now
    active = forms.BooleanField(label=_("Évènement non fini"))
    active.required = False
    description = forms.CharField(label=_("Description"))
    ville = forms.CharField(label=_("Ville"))


class AfficheEvent(forms.Form):
    actif = forms.BooleanField(label=_("Afficher les evenements non actifs"))
    actif.required = False
    actif.initial = False
    moi = forms.BooleanField(label=_("Sélectionner mes évènements"))
    moi.required = False
    moi.initial = False
    ville_form = forms.CharField(label=_("Ville"))
    ville_form.required = False
