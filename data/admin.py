from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import person


admin.site.register(person)

# Register your models here.
