from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'bio',
                    'role',
                    'confirmation_code')
    list_filter = ('role',)


admin.site.register(User, CustomUserAdmin)
