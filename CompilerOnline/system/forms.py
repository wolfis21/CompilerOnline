from django import forms
from .models import Roles

class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['name_rol']