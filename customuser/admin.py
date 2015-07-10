from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from forms import UserCreationForm, UserChangeForm
from models import User, Activation


# Register your models here.
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone', 'ampluas', 'avatar')}),
        ('Permissions',
         {'fields': ('is_active', 'is_referee', 'is_coach', 'is_responsible', 'is_organizer', 'is_admin', 'is_staff', 'is_superuser')}),
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
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_filter = ('is_active', 'is_referee', 'is_coach', 'is_responsible', 'is_organizer', 'is_admin', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('ampluas',)


class ActivationAdmin(admin.ModelAdmin):
    model = Activation
    readonly_fields = ['email', 'status', 'token', 'datetime']
    # read only rules
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register the new EmailUserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Activation, ActivationAdmin)