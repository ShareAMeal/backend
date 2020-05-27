from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError
from PIL import Image


class User(AbstractUser):
    pass


class Association(models.Model):

    user = models.OneToOneField(to=User, related_name='association', on_delete=models.CASCADE)
    contact_email = models.EmailField(unique=True, verbose_name="Contact email")
    name = models.CharField(unique=True, verbose_name="Name", max_length=127)
    location = models.CharField(verbose_name="Address", blank=True, null=True, max_length=1023)
    description = models.TextField()
    phone = models.CharField(blank=True, null=True, verbose_name="Phone number", max_length=15)
    image = models.ImageField(default='default.jpg', upload_to='asso_pics')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Event(models.Model):
    class Meta:
        verbose_name = "Event"

    organizer = models.ForeignKey(to=Association, verbose_name="Organizer", related_name='events',
                                  on_delete=models.DO_NOTHING)
    # mettre latitude longitude
    name = models.CharField(verbose_name="Name", max_length=63)
    start_datetime = models.DateTimeField(default=timezone.now, verbose_name="Starting Date and Time")
    end_datetime = models.DateTimeField(null=True, verbose_name="Ending date and time")
    active = models.BooleanField(default=True, verbose_name="Active")
    description = models.TextField(blank=True, verbose_name="Description")
    location = models.CharField(blank=True, verbose_name="Location", max_length=200)

    def __str__(self):
        return f"{self.name} by {self.organizer.name}"

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def clean(self):
        if self.end_datetime <= self.start_datetime:
            raise ValidationError('Ending times must after starting times')
