from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User
import logging
log = logging.getLogger(__name__)
# convert the errors to text
from django.utils.encoding import force_text

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','nickname', 'petname', 'petkind', 'is_admin', 'profile')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',)}),
        ('Personal info', {'fields': ('nickname', 'petname', 'petkind','profile')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'petname', 'petkind', 'password1', 'password2', 'profile')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    def is_valid(self):
        log.info(force_text(self.errors))
        return super(UserAdmin, self).is_valid()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
