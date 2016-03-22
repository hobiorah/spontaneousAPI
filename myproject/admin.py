from django.contrib import admin
from .models import DPUser
from .models import Preference

admin.site.register(DPUser)
admin.site.register(Preference)