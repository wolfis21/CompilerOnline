from django.contrib import admin
from .models import Roles
from .models import Students
from .models import Users
from .models import Projects
from .models import Container

@admin.register(Roles)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','name_rol')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """

@admin.register(Students)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'last_name', 'question_u', 'response_u', 'users_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','name_u', 'email', 'password', 'roles_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Projects)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion', 'data_ref', 'check_complete', 'created', 'updated', 'container_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Container)

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created', 'updated', 'students_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """


