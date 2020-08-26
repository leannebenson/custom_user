

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_app.models import BaseUser
# Register your models here.
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('display_name', 'age', 'homepage')}),

admin.site.register(BaseUser, UserAdmin)