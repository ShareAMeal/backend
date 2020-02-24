from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
class Assocation(models.Model):
    contact_email = models.EmailField(unique=True, verbose_name="Email de contact")
    name = models.CharField(unique=True, verbose_name="Nom")
    location = models.CharField(verbose_name="Adresse", blank=True, null=True)
    description = models.TextField()
    phone = models.CharField(blank=True, null=True, verbose_name="N° de téléphone")
    admin = models.OneToOneField(to=User, related_name='association', on_delete=models.CASCADE)

class Event(models.Model):
    organisateur = models.ForeignKey(to=Assocation, verbose_name="Organisateur",
                                     null=True, blank=True, related_name='events')
    # latitude longitude
    nom = models.CharField(verbose_name="Nom")
    datetime = models.DateTimeField()
    actif = models.BooleanField()
    description = models.TextField()