from django import forms
from .models import *

class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['name_rol']

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name_u', 'email', 'password', 'roles_id']