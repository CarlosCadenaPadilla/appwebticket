from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    #muestra los campos en el administrador
    readonly_fields = ('created','updated')

admin.site.register(Event,EventAdmin)