from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from api import models


# Register your models here.
@admin.register(models.Association)
class AssoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)

