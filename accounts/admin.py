from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RamenUser
from django.contrib.auth import get_user_model 

from .forms import RamenUserCreationForm, RamenUserChangeForm

class RamenAdmin(UserAdmin):
    add_form = RamenUserCreationForm
    form = RamenUserChangeForm
    model = RamenUser
    list_display = ['email', 'username']



admin.site.register(RamenUser, RamenAdmin)

# Register your models here.
