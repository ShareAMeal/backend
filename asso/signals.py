from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import  receiver
from api.models import Association

User = get_user_model()


@receiver(post_save, sender=User)
def create_asso(sender, instance, created, **kwargs):
    if created:
        Association.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_asso(sender, instance, **kwargs):
    instance.association.save()