from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Registro el modelo para administralo desde el admin de Djanago
from users.models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phone_numbers', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_numbers', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__firs_name',
        'user__last_name',
        'phone_numbers',
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'modified'
    )
    filedsets = (
   ('Profile', { 
        'fields':(('user','pictures'),),
    }),
     ('Extra info',{
        'fields':(
            ('website','phone_numbers'),
            ('biography')
        )
    }),
    ('Metadata',{
        'fields':(('created','modified'),),
    })
    
)
readonly_field = ('created','modified',)

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):

        inlines = (ProfileInline,)
        list_display = (
            'username',
            'email',
            'first_name',
            'is_active',
            'is_staff'
        )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
