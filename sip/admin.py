from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# class EventAdmin(admin.ModelAdmin):


admin.site.register(User, UserAdmin)
admin.site.register(Event)
admin.site.register(Product)



