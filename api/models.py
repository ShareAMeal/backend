from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    pass


class Association(models.Model):
    contact_email = models.EmailField(unique=True, verbose_name=_("Email de contact"))
    name = models.CharField(unique=True, verbose_name=_("Nom"), max_length=127)
    location = models.CharField(verbose_name=_("Adresse"), blank=True, null=True, max_length=1023)
    description = models.TextField()
    phone = models.CharField(blank=True, null=True, verbose_name=_("N° de téléphone"), max_length=15)
    admin = models.OneToOneField(to=User, related_name='association', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        verbose_name = "Évènement"

    organizer = models.ForeignKey(to=Association, verbose_name=_("Organisateur"), related_name='events',
                                  on_delete=models.CASCADE)
    # mettre latitude longitude
    name = models.CharField(verbose_name="Nom", max_length=63)
    start_datetime = models.DateTimeField(default=timezone.now, verbose_name="Date de début")
    active = models.BooleanField(default=True, verbose_name="Évènement non fini")
    description = models.TextField(blank=True, verbose_name="Description")
    ville = models.TextField(blank=True, verbose_name="Ville")

    def __str__(self):
        return f"{self.name} par {self.organizer.name}"
