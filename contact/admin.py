from django.contrib import admin
from .models import Message, Remessage

# Register your models here.
admin.site.register(Message)
admin.site.register(Remessage)