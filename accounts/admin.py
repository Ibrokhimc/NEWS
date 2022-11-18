from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import CustomUser
from .forms import CustomChangeForm, CustomUserCreationForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['age']}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ['age']}),
    )

admin.site.register(CustomUser, CustomUserAdmin)