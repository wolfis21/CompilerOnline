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

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'last_name', 'question_u', 'response_u', 'users_id']

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['title']
        labels = {
            'title': 'Título',
        }