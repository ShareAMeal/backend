from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from web import models
# Register your models here.
@admin.register(models.Assocation)
class AssoAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.User, UserAdmin)