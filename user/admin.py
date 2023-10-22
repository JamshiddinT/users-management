from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, UserCreationForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'email', 'status', 'date_joined']
    # fieldsets = UserAdmin.fieldsets +(
    #     (None, {'fields':('age','linkedin')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets +(
    #     (None, {'add_fields':('age','linkedin')}),
    # )

admin.site.register(CustomUser,CustomUserAdmin)