from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from forms import UserCreationForm, UserChangeForm
from models import User


# Register your models here.
class UserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_responsible', 'is_staff', 'is_admin', 'is_superuser')}),
        ('Optional', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
    ),
    )

    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_responsible', 'is_staff', 'is_admin', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Register the new EmailUserAdmin
admin.site.register(User, UserAdmin)