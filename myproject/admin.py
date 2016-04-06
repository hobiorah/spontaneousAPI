from django.contrib import admin
from .models import DPUser
from .models import Preference
from .models import Favorite
from .models import Visited

admin.site.register(DPUser)
admin.site.register(Preference)
admin.site.register(Favorite)
admin.site.register(Visited)