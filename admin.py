from django.contrib import admin

from .models import Penalty
from .models import Profile
# Register your models here.

admin.site.register(Penalty)
admin.site.register(Profile)
