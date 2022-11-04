from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
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
                  'role')

admin.site.register(User, CustomUserAdmin)