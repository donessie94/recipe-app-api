"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
#this one imports all the custom models we wrote and want to register with Django admin
from core import models


# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    #BTW all these fields are already defined in BaseUserAdmin we just giving them customize values that we want
    #(of course using the documentation syntax for Django admin and the database we created for the syntax and name of the values)

    #this will order the user by id
    ordering = ['id']
    #the fields we want to display in the admin website
    list_display = ['email', 'name']

    #
    fieldsets = ( (None, {'fields': ('email', 'password') }),
                  (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser') }),
                  (_('Important Dates'), {'fields': ('last_login',) })
    )
    readonly_fields = ['last_login']

    add_fieldsets = ( (None, {'classes': ('wide',),
                              'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser')
                             }),
    )

#we need the second argument "UserAdmin" to make sure it assigns the custom model manager we wrote above
#instead of the default one
admin.site.register(models.User, UserAdmin)

